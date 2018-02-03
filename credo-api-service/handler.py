from validator import validate, ValidationException

import config

def handle_detection(message):
    validate(message)
    sendmessage(message)


def sendmessage(message):
    pass
