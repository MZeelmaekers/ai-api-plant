from urllib import request
import fastbook
fastbook.setup_book()
from fastbook import *
from fastai.vision.widgets import *
from flask import Flask, jsonify

app = Flask(name)


@app.route('/', methods['POST'])
def get_result():
    aipredict = load_learner('./groeistadiamodel.pkl')
    photo = request.files['file']
    prediction = aipredict.predict(photo)

    json_file = {}
    json_file['query'] = prediction
    return jsonify(json_file)

@app.route('/', methods['GET'])
def index():
  return "<h1>Welcome to the Plant AI</h1>"



