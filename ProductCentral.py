from ProductCard import (
    ProductCard,
)

class ProductCentral:
    """Класс для управления карточками товаров."""

    def __init__(self):
        """Инициализация пустого списка и сброс индекса"""

        self.cards = []
        self.current_card_index = -1

    def add_card(self, card: ProductCard) -> None:
        """Метод для добавления карточки в список.

        Args:
            card: обьект карточки товара
        """

        self.cards.append(card)
        print('Карточка добавлена.')

    def select_card(self, index: int) -> bool:
        """Выбор текущей карточки по индексу.

        Args:
            index: индекс карточки в данном списке
        """

        if 0 <= index < len(self.cards):
            self.current_card_index = index

            return True
        return False

    def get_current_card(self) -> ProductCard:
        """Получение текущей карточки.

        Returns:
            ProductCard: Карточку товара или none если не выбрана
        """

        if 0 <= self.current_card_index < len(self.cards):
            return self.cards[self.current_card_index]
        return None

    def print_cards_list(self) -> None:
        """Вывод списка всех карточек."""

        if not self.cards:
            print("Список карточек пуст.")
            return

        print("СПИСОК КАРТОЧЕК ТОВАРОВ")
        i = 0

        while i < len(self.cards):
            card = self.cards[i]
            print(f" {i}: {card.get_name()} (ID: {card.get_card_id()}) - {card.get_status()}")
            i += 1
