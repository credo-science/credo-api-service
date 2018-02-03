# do some basic validation

REQUIRED_FIELDS = ['body', 'header']


def validate(message):
    if REQUIRED_FIELDS not in message.keys():
        raise Exception("A required field is missing!")

    return False
