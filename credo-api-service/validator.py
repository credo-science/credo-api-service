# do some basic validation

REQUIRED_FIELDS = ['body', 'header']


class ValidationException(Exception):
    pass


def validate(message):
    if REQUIRED_FIELDS not in message.keys():
        raise ValidationException("A required field is missing!")

    return False
