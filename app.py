from flask import Flask, jsonify, request, escape, render_template
from flask_cors import CORS
from compare_reddits import compareSubList, compareTwoSubs
import json

with open('data/stored_descs.json', 'r') as store:
    stored_descs = json.load(store)

app = Flask(__name__)
CORS(app)



@app.route('/getlinks', methods=['POST'])
def get_links():
    if request.method == 'POST':
        subs = request.form.getlist('subreddits[]')
        return jsonify(compareSubList(','.join(subs), stored_descs))
    else:
        return jsonify({})

@app.route('/checksub=<name>', methods=['GET'])
def check_sub(name):
    if name.lower() in stored_descs:
        return 'valid'
    else:
        return 'invalid'

@app.route('/')
def retIndex():
    return render_template('index.html')