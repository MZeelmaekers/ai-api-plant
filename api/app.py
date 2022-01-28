from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from PIL import Image
from fastai.vision.all import *
from flask import *
import pathlib
plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

app = Flask(__name__)

@app.route('/result', methods=["POST"])
def result():
    aipredict = load_learner('./laatstemodel.pkl')
    photo = request.files['file']

    connect_str = "DefaultEndpointsProtocol=https;AccountName=storagemainfotosplanten;AccountKey=YHIqjHCcXi8IO3DabS+N1lRzrBoltBaDDofu9vJmMo2tMQghoHMQ8fKT/GXVD0Q569EW8pfuJVqv7CjVkPreVA==;EndpointSuffix=core.windows.net'"
    blob = BlobClient.from_connection_string(conn_str=connect_str, container_name="storagemainfotosplanten", blob_name="botanic")
    with open("./"+ photo, "wb") as my_blob:
        blob_data = blob.download_blob()
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

