import fastbook
fastbook.setup_book()
from fastbook import *
from fastai.vision.widgets import *
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/result', methods["POST"])
def result():
    aipredict = load_learner('./laatstemodel.pkl')
    photo = request.files['file']
    prediction = aipredict.predict(photo)

    json_file = {}
    json_file['prediction'] = prediction
    return jsonify(json_file)

@app.route('/')
def index():
  return "<h1>Welcome to the Plant AI</h1>"

if __name__ == "__main__":
  app.run()

