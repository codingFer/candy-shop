import re

from django.core.exceptions import ValidationError


def validar_par(value):
    if value % 2 != 0:
        # raise ValidationError("El par debe ser par")
        raise ValidationError('%(value)s no es un numero par', params={"value":
                                                                           value})


def validar_nombre(value):
    if value == "Comida":
        raise ValidationError('%(value)s no es un texto permitido',
                              params={"value": value})


def positive_value(value):
    if value <= 0:
        raise ValidationError('%(value)s no es un numero positivo', )

def bolivian_phone_number(number):
    # Número debe comenzar con 7, 6 o 2 seguido de 7 dígitos
    bolivian_regex = re.compile(r'^(?:7|6)\d{7}$')

    if not bolivian_regex.match(number):
        raise ValidationError(
            "El número de teléfono no es válido para Bolivia. Debe comenzar con 7 o 6 y tener 8 dígitos.")

    return number
