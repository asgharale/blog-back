from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


def email_validation(email):
    try:
        validate_email(email)
        return email
    except:
        raise ValidationError("Enter An valid email please.")
    # if validate_email(email):
    #     return email
    # raise ValidationError("Enter An valid email please.")


def user_validation(clean_data):
    user = authenticate(
        email = clean_data['email'],
        password = clean_data['password']
    )
    if not user:
        raise ValidationError('user not found.')
    return user