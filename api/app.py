from fastai.vision.all import *
from flask import *

app = Flask(__name__)

@app.route('/result', methods=["POST"])
def result():
    aipredict = load_learner(open('./laatstemodel.pkl','rb'))
    photo = request.files['file']
    prediction = aipredict.predict(photo)


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

