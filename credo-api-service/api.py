from flask import Flask, request

from validator import validate

app = Flask(__name__)


@app.route('/detection', methods=['GET', 'POST'])
def detection():
    try:
        message = request.get_json(force=True)
    except Exception, e:
        return "Message was not a proper json", 422

    try:
        handle_detection(message)
    except Exception, e:
        pass

    return


def sendmessage():
    pass


def handle_detection(message):
    validate(message)
    sendmessage(message)
