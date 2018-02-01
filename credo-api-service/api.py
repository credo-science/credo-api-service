from flask import Flask, request

app = Flask(__name__)


@app.route('/detection', methods=['GET', 'POST'])
def detection():
    return request.get_data()
