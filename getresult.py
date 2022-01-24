from flask import Flask, request, jsonify, render_template, url_for
app = Flask(__name__)

@app.route('/home')
def home():
    return 'Hello World'


app.run(host='0.0.0.0',port=5000)



