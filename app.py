# from fastai.vision import *
from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)


@app.route('/result', methods["POST"])
def result():
    # aipredict = load_learner('./laatstemodel.pkl')
    model= joblib.load(open("laatstemodel.pkl", "rb"))
    photo = request.files['file']
    prediction = model.predict(photo)

    json_file = {}
    json_file['prediction'] = prediction
    return jsonify(json_file)

@app.route('/')
def index():
  return "<h1>Welcome to the Plant AI</h1>"

if __name__ == "__main__":
  app.run()

