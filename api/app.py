from logging import DEBUG
from flask import Flask, jsonify, request
from flask.wrappers import Response
from flask_cors import CORS
from werkzeug.wrappers import response

# configuration

BOOKS = [
    {
        'title': 'On the road',
        'author' : 'Jack lassle',
        'read': True,
        'price': 1000
    },
    {
        'title': 'Gone of the win',
        'author' : 'Harry john',
        'read': True,
        'price': 1100
    },
    {
        'title': 'Harry portter',
        'author' : 'Jam swait',
        'read': True,
        'price': 500
    }
]

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

#enable Cors

CORS(app, responses={r'*' : {'origins': '*'} })

# sanity check route

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 200,
        'books': BOOKS
    })

@app.route('/books', methods=['POST'])
def save_book():

    response_object = {'status': 201}

    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
            'price': post_data.get('price')
        })
        response_object['message'] = 'Book added!'
        return jsonify(response_object)
if __name__ == '__main__':
    app.run()