import binascii
import io
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

    # r_data = binascii.unhexlify(photo)

    # stream = io.BytesIO(r_data)

    img = Image.open(photo)

    prediction = aipredict.predict(img)


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

