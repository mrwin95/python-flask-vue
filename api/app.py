from logging import DEBUG
from flask import Flask, jsonify
from flask.wrappers import Response
from flask_cors import CORS

# configuration

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

#enable Cors

CORS(app, responses={r'*' : {'origins': '*'} })

# sanity check route

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

if __name__ == '__main__':
    app.run()