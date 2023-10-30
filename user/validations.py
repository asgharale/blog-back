from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def email_validate(email):
    try:
        validate_email(email)
        return email
    except:
        raise ValidationError("Enter An valid email please.")
    # if validate_email(email):
    #     return email
    # raise ValidationError("Enter An valid email please.")
