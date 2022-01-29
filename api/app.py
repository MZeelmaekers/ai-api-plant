from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from PIL import Image
from fastai.vision.all import *
from flask import *
import pathlib
plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

app = Flask(__name__)

connect_str = "DefaultEndpointsProtocol=https;AccountName=storagemainfotosplanten;AccountKey=YHIqjHCcXi8IO3DabS+N1lRzrBoltBaDDofu9vJmMo2tMQghoHMQ8fKT/GXVD0Q569EW8pfuJVqv7CjVkPreVA==;EndpointSuffix=core.windows.net'"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container_name = 'botanic'
container_client = blob_service_client.get_container_client(container_name)

@app.route('/result', methods=["POST"])
def result():
    aipredict = load_learner('./laatstemodel.pkl')
    photo = request.form.get("file")
    
    with open("./"+ photo, "wb") as my_blob:
        blob_data = container_client.download_blob()
        blob_data.readinto(my_blob)

    

    prediction = aipredict.predict(blob_data)


    week = prediction[0] 
    accuracyprediction = re.search('TensorBase(.*)', str(max(prediction[2])))
    accuracypr = accuracyprediction.group(1).strip('(').strip(')')


    json_file = {}
    json_file['week'] = week
    json_file['accuracy'] = accuracypr

    return jsonify(json_file)

@app.route('/test')
def test():
    json_file = {}
    json_file['hello'] = 'hello world'
    return jsonify(json_file)

@app.route('/')
def index():
  return "<h1>Welcome to the Plant AI</h1>"

if __name__ == '__main__':
  app.run(debug=True)

