import os
from PIL import Image
from fastai.vision.all import *
from flask import *
import pathlib
from matplotlib import transforms
from azure.storage.blob import BlobServiceClient, __version__
from multiprocessing.pool import ThreadPool
import pathlib


plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath


connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container = "modelbotanic"
localblobpath = "./"

class AzureBlobFileDownloader():
  def __init__(self, container):
    self.blob_service_client =  BlobServiceClient.from_connection_string(connect_str)
    self.my_container = self.blob_service_client.get_container_client(container)
 
  def download_all_blobs_in_container(self):
    my_blobs = self.my_container.list_blobs()
    result = self.run(my_blobs)
 
  def run(self,blobs):
    with ThreadPool(processes=int(10)) as pool:
     return pool.map(self.save_blob_locally, blobs)
 

  def save_blob_locally(self, blob):
    file_name = blob.name
    bytes = self.my_container.get_blob_client(blob).download_blob().readall()
 
    download_file_path = os.path.join(localblobpath, file_name)

    os.makedirs(os.path.dirname(download_file_path), exist_ok=True)
 
    with open(download_file_path, "wb") as file:
      file.write(bytes)
    return file_name


app = Flask(__name__) 

@app.route('/result', methods=["GET", "POST"])
def result():

  if not os.path.exists('./AI-model.pkl'):
    azure_blob_file_downloader = AzureBlobFileDownloader(container)
    azure_blob_file_downloader.download_all_blobs_in_container()
  


  aipredict = load_learner('./AI-model.pkl')

  photo = request.files["file"]
  image = PILImage.create(photo)
        
  prediction = aipredict.predict(image)


  week = prediction[0] 
  accuracyprediction = re.search('TensorBase(.*)', str(max(prediction[2])))
  accuracypr = accuracyprediction.group(1).strip('(').strip(')')


  json_file = {}
  json_file['week'] = week
  json_file['accuracy'] = accuracypr

  return jsonify(json_file)


@app.route('/')
def index():
  return "<h1>Welcome to the Plant AI</h1>"

if __name__ == '__main__':
  app.run(debug=True)








