class ProductCardError(Exception):
    pass


class InvalidNameError(ProductCardError):
    pass


class InvalidQuantityError(ProductCardError):
    pass


class InvalidStatusError(ProductCardError):
    pass


class InvalidProviderError(ProductCardError):
    pass


class InvalidManufacturerError(ProductCardError):
    pass


class InvalidPriceError(ProductCardError):
    pass


class InvalidWeightError(ProductCardError):
    pass


class InvalidLocationError(ProductCardError):
    pass


class InvalidCardIDError(ProductCardError):
    pass


class WriteOffError(ProductCardError):
    pass


class InvalidReasonError(ProductCardError):
    pass
