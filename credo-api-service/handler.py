from validator import validate, ValidationException


def handle_detection(message):
    validate(message)
    sendmessage(message)


def sendmessage(message):
    pass
