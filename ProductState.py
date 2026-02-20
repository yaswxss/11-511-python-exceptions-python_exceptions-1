class ProductState:
    """Класс для управления статусами карточек товара"""

    accepted = "Принято к учёту"
    in_stock = "Состоит на учёте"
    damaged = "Повреждено"
    expired = "Просрочено"
    written_off = "Списано"

    def __init__(self):
        """Инициализация/конструктор класса, списков статусов"""

        self.all_states = [
            self.accepted,
            self.in_stock,
            self.damaged,
            self.expired,
            self.written_off
        ]
        self.write_off_allowed_states = [
            self.accepted,
            self.in_stock
        ]

    def get_all_states(self):
        """Геттер для получения всевозможных статусов карты продукта

        Returns:
            all_states: Все возможные статусы продукта
        """

        return self.all_states

    def get_write_off_allowed_states(self):
        """Геттер для получения статусов, из которых возможно списание

        Returns:
            write_off_allowed_states: Все статусы, из которых можно списать продукты
        """

        return self.write_off_allowed_states

    def is_write_off_allowed(self, state: str) -> bool:
        """Метод для определения можно ли списать карточку с данного статуса

        Returns:
            True|False
        """

        return state in self.write_off_allowed_states
