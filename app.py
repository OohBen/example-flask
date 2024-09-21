from flask import Flask, request, jsonify
import requests
import webvtt
# Flask app
app = Flask(__name__)
@app.route("/get", methods=["GET"])
def file_get():
    url = request.args.get('url')
    resp = requests.get(url)
    vtt = webvtt.from_string(resp.text)
    # Return the content in json format
    # get only the text from the vtt file in one long string
    data = {'text': ' '.join([c.text for c in vtt.captions])}['text']
    return str(data)

