# do some basic validation

REQUIRED_FIELDS = {u'body', u'header'}


class ValidationException(Exception):
    pass


def validate(message):
    if not REQUIRED_FIELDS.issubset(set(message.keys())):
        raise ValidationException("A required field is missing!")

    return False
