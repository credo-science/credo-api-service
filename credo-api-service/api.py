from flask import Flask, request

from handler import handle_detection
from validator import ValidationException

app = Flask(__name__)


@app.route('/detection', methods=['POST'])
def detection():
    try:
        message = request.get_json(force=True)
    except Exception, e:
        return "Message was not a proper json", 422

    try:
        handle_detection(message)
    except ValidationException, e:
        return "The message contained invalid data: " + str(e), 422
    except Exception, e:
        return "There was a problem while processing the message: " + str(e), 500

    return "", 200
