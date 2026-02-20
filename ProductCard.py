from ProductState import (
    ProductState,
)
from ProductExceptions import *


class ProductCard:
    """Класс для описания карты продукта"""

    def __init__(
            self,
            name : str = 'NA',
            quantity : int = None,
            status: str = ProductState.accepted,
            provider: str = 'NA',
            manufacturer: str = 'NA',
            price: int = None,
            weight: int = None,
            category: str = 'NA',
            location: str = 'NA',
            shelflife: int = None,
            cardID: str = 'NA',
            note: str = 'NA',
    )-> None:

        """Инициализация/конструктор класса карточки товара

        Args:
            name: Наименование продукта
            quantity: Количество продукта
            status: Статус продукта
            provider: Поставщик продукта
            manufacturer: Производитель продукта
            price: Цена продукта
            weight: Вес продукта
            category: Категория продукта
            location: Локация продукта
            shelflife: Срок годности
            cardID: Айди карты
            note: Дополнительные сведения
        """


        self.__name = name
        self.__quantity = quantity
        self.__status = status
        self.__provider = provider
        self.__manufacturer = manufacturer
        self.__price = price
        self.__weight = weight
        self.__category = category
        self.__location = location
        self.__shelflife = shelflife
        self.__cardID = cardID
        self.__note = note

    def set_name(self, name: str) -> None:
        """Сеттер для имени

        Args:
            name: Наименование продукта
        """

        if not name or len(name.strip()) < 1:
            raise InvalidNameError("Имя карточки не может быть пустым")
        self.__name = name

    def get_name(self) -> str:
        """Геттер для имени

        Returns:
            name: Наименование продукта
        """

        return self.__name

    def set_quantity(self, quantity: int)-> None :
        """Сеттер для количество

        Args:
            quantity: Количество продукта
        """

        if quantity < 0:
            raise InvalidQuantityError("Количество товара не может быть отрицательным")
        self.__quantity = quantity

    def get_quantity(self) -> int:
        """Геттер для количества

        Returns:
            quantity: Количество продукта
        """

        return self.__quantity

    def set_status(self, status: str) -> None:
        """Сеттер для статуса

        Args:
            status: Статус продукта
        """

        state_check = ProductState()
        if status not in state_check.get_all_states():
            raise InvalidStatusError("Недопустимое состояние")
        self.__status = status

    def get_status(self) -> str:
        """Геттер для статуса

        Returns:
            status: Статус продукта
        """

        return self.__status

    def set_provider(self, provider: str) -> None:
        """Сеттер для поставщика

        Args:
            provider: Поставщик продукта
        """

        if not provider or len(provider.strip()) < 1:
            raise InvalidProviderError("Имя поставщика не может быть пустым")
        self.__provider = provider

    def get_provider(self) -> str:
        """Геттер для поставщика

        Returns:
            status: Поставщик продукта
        """

        return self.__provider

    def set_manufacturer(self, manufacturer: str) -> None:
        """Сеттер для производителя

        Args:
            manufacturer: Производитель продукта
        """

        if not manufacturer or len(manufacturer.strip()) < 1:
            raise InvalidManufacturerError("Имя производителя не может быть пустым")
        self.__manufacturer = manufacturer

    def get_manufacturer(self) -> str:
        """Геттер для производителя

        Returns:
            status: Производитель продукта
        """

        return self.__manufacturer

    def set_price(self, price: int)-> None :
        """Сеттер для цены

        Args:
            price: Цена продукта
        """

        if price < 0:
            raise InvalidPriceError("Цена товара не может быть отрицательной")
        self.__price = price

    def get_price(self) -> int:
        """Геттер для цены

        Returns:
            price: Цена продукта
        """

        return self.__price

    def set_weight(self, weight: int)-> None :
        """Сеттер для веса

        Args:
            weight: Вес продукта
        """

        if weight < 0:
            raise InvalidWeightError("Вес товара не может быть отрицательным")
        self.__weight = weight

    def get_weight(self) -> int:
        """Геттер для веса

        Returns:
            price: Вес продукта
        """

        return self.__weight

    def set_category(self, category: str) -> None:
        """Сеттер для категории

        Args:
            category: Категория продукта
        """

        self.__category = category

    def get_category(self) -> str:
        """Геттер для категории

        Returns:
            category: Категория продукта
        """

        return self.__category

    def set_location(self, location: str) -> None:
        """Сеттер для локации

        Args:
            location: Локация продукта
        """

        if not location or len(location.strip()) < 1:
            raise InvalidLocationError("Локация не может быть пустым")
        self.__location = location

    def get_location(self) -> str:
        """Геттер для локации

        Returns:
            location: Локация продукта
        """

        return self.__location

    def set_shelflife(self, shelflife: int) -> None:
        """Сеттер для срока годности

        Args:
            shelflife: Срок годности продукта
        """

        self.__shelflife = shelflife

    def get_shelflife(self) -> int:
        """Геттер для срока годности

        Returns:
            shelflife: Срок годности продукта
        """

        return self.__shelflife

    def set_cardID(self, cardID: str) -> None:
        """Сеттер для айди карты

        Args:
            cardID: Айди карты продукта
        """

        if not cardID or len(cardID.strip()) < 1:
            raise InvalidCardIDError("ID карточки не может быть пустым")
        self.__cardID = cardID

    def get_card_id(self) -> str:
        """Геттер для айди карты

        Returns:
            cardID: Айди карты продукта
        """

        return self.__cardID

    def set_note(self, note: str) -> None:
        """Сеттер для дополнительной информации

        Args:
            note: Дополниельные сведения продукта
        """

        self.__note = note

    def get_note(self) -> str:
        """Геттер для дополнительных сведений карты

        Returns:
            note: Дополнительные сведения продукта
        """

        return self.__note

    def write_off(self, reason: str) -> None:
        """Метод списания карточки товара по причине"""

        state_check = ProductState()
        if self.__status not in state_check.get_write_off_allowed_states():
            raise WriteOffError(f"Невозможно списать карточку в состоянии '{self.__status}'.")
        if not reason or len(reason.strip()) < 3:
            raise InvalidReasonError("Причина списания должна содержать минимум 3 символа")
        self.__status = ProductState.written_off
        print("Карточка успешно списана.")

    def is_written_off(self) -> bool:
        """Метод для проверки списана ли карта"""

        return self.__status == ProductState.written_off

    def reset(self) -> None:
        """Метод для сброса значений по умолчанию"""

        self.__name = 'NA'
        self.__quantity = 0
        self.__status = ProductState.accepted
        self.__provider = 'NA'
        self.__manufacturer = 'NA'
        self.__price = 0
        self.__weight = 0
        self.__category = 'NA'
        self.__location = 'NA'
        self.__shelflife = 0
        self.__cardID = 'NA'
        self.__note = 'NA'

    def print_info(self) -> None:
        """Вывод полной информации о карточке."""

        print(
            f'Наименование: {self.__name}\n'
            f'Количество: {self.__quantity}\n'
            f'Состояние: {self.__status}\n'
            f'Поставщик: {self.__provider}\n'
            f'Производитель: {self.__manufacturer}\n'
            f'Цена: {self.__price}\n'
            f'Вес: {self.__weight}\n'
            f'Категория: {self.__category}\n'
            f'Местоположение: {self.__location}\n'
            f'Срок годности: {self.__shelflife}\n'
            f'ID карточки: {self.__cardID}\n'
            f'Примечание: {self.__note}\n'
        )
