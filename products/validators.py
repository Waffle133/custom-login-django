from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible


@deconstructible
class SkuValidator(RegexValidator):
    regex = r'[A-Z]{2}-[\d]{3}-[\d]{3}\Z'
    message = 'Enter a SKU, use the format XX-###-### .'
    flags = 0


validate_sku = RegexValidator(
    regex=r'[A-Z]{2}-[\d]{3}-[\d]{3}\Z',
    message='El SKU que ingresas no es correcto, debe de seguir la nomenclatura XX-###-### .'
)


def sku_validator(value):
    return validate_sku(value)
