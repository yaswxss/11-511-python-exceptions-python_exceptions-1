from ProductState import (
    ProductState,
)

from ProductCard import (
    ProductCard,
)

from ProductCentral import (
    ProductCentral,
)

from ProductExceptions import *


class ProductFace:
    """Класс для красивого UI работы с карточками товаров."""

    def __init__(self):
        """Инициализация интерфейса."""

        self.manager = ProductCentral()
        self._create_sample_cards()

    def _create_sample_cards(self) -> None:
        """Создание примеров карточек."""

        try:
            card1 = ProductCard(
                name = "Ноутбук",
                quantity = 52,
                status = ProductState.accepted,
                provider = "ООО Apple",
                manufacturer = "Apple",
                price = 150000,
                weight = 2000,
                category = "Электроника",
                location = "Казань.Баумана.",
                shelflife = 730,
                cardID = "CARD001",
                note = "Гарантия 3 года"
            )

            card2 = ProductCard(
                name = "Мышь беспроводная",
                quantity = 20,
                status = ProductState.in_stock,
                provider = "ООО Android",
                manufacturer = "Android",
                price = 1500,
                weight = 100,
                category = "Аксессуары",
                location = "Москва.Бауманская.",
                shelflife = 365,
                cardID = "CARD002",
                note = "Батарейки не входят"
            )

            self.manager.add_card(card1)
            self.manager.add_card(card2)
            self.manager.select_card(0)
        except Exception as e:
            print(f"Ошибка при создании тестовых карточек: {e}")

    def print_main_menu(self) -> None:
        """Вывод главного меню."""

        print("Управление карточками товаров")

        current = self.manager.get_current_card()
        if current:
            print(f"Текущая карточка: {current.get_name()} (ID: {current.get_card_id()})")
            print(f"Статус: {current.get_status()}")
        else:
            print("Текущая карточка: не выбрана")

        print(
            '\n1: Создать карточку.\n'
            '2: Выбрать карточку.\n'
            '3: Список карточек\n'
            '4: Показать карточку\n'
            '5: Изменить карточку\n'
            '6: Списать карточку\n'
            '0: ВЫХОД\n'
        )

    def create_card_interactive(self) -> None:
        """Создание новой карточки."""

        print('Создание карточки товара')

        try:
            name = input("Наименование: ")
            quantity = int(input("Количество: "))

            print("Доступные статусы:")
            print("0: Принято к учёту")
            print("1: Состоит на учёте")
            print("2: Повреждено")
            print("3: Просрочено")
            print("4: Списано")

            status_choice = int(input("Выберите статус (0-4): "))
            states = ProductState().get_all_states()
            status = states[status_choice]

            provider = input("Поставщик: ")
            manufacturer = input("Производитель: ")
            price = int(input("Цена: "))
            weight = int(input("Вес: "))
            category = input("Категория: ")
            location = input("Местоположение: ")
            shelflife = int(input("Срок годности (дней): "))
            cardID = input("ID карточки: ")
            note = input("Дополнительные сведения: ")

            new_card = (ProductCard(
                name = name,
                quantity = quantity,
                status = status,
                provider = provider,
                manufacturer = manufacturer,
                price = price,
                weight = weight,
                category = category,
                location = location,
                shelflife = shelflife,
                cardID = cardID,
                note = note
            ))

            self.manager.add_card(new_card)
            print("Карточка создана!")

        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except ProductCardError as e:
            print(f"Ошибка карты продукта: {e}")
        except IndexError:
            print("Неверный выбор статуса!")

    def select_card_interactive(self) -> None:
        """Выбор карточки из списка."""

        self.manager.print_cards_list()

        if self.manager.cards:
            try:
                index = int(input("Введите индекс: "))
                if self.manager.select_card(index):
                    current = self.manager.get_current_card()
                    print(f"Выбрано: {current.get_name()}")
                else:
                    print("Неверный индекс!")
            except ValueError:
                print("Ошибка ввода!")

    def show_current_card(self) -> None:
        """Показать информацию о текущей карточке."""

        current = self.manager.get_current_card()
        if current:
            current.print_info()
        else:
            print("Карточка не выбрана!")

    def change_current_card(self) -> None:
        """Изменить параметры текущей карточки."""

        current = self.manager.get_current_card()
        if not current:
            print("Сначала выберите карточку!")
            return

        print("ИЗМЕНЕНИЕ КАРТОЧКИ")
        print(
            '\n1: Наименование\n'
            '2: Количество\n'
            '3: Статус\n'
            '4: Поставщик\n'
            '5: Производитель\n'
            '6: Цена\n'
            '7: Вес\n'
            '8: Категория\n'
            '9: Местоположениe\n'
            '10: Срок годности\n'
            '11: Айди карты\n'
            '12: Дополнительные сведения\n'
        )

        try:
            choice = input("Выберите  (1-12): ")
            if choice == "1":
                new = input("Новое наименование: ")
                current.set_name(new)
            elif choice == "2":
                new = int(input("Новое количество: "))
                current.set_quantity(new)
            elif choice == "3":
                state_obj = ProductState()
                states = state_obj.get_all_states()
                print("0: Принято к учёту")
                print("1: Состоит на учёте")
                print("2: Повреждено")
                print("3: Просрочено")
                print("4: Списано")
                idx = int(input("Выберите статус (0-4): "))
                current.set_status(states[idx])
            elif choice == "4":
                new = input("Новый поставщик: ")
                current.set_provider(new)
            elif choice == "5":
                new = input("Новый производитель: ")
                current.set_manufacturer(new)
            elif choice == "6":
                new = int(input("Новая цена: "))
                current.set_price(new)
            elif choice == "7":
                new = int(input("Новый вес: "))
                current.set_weight(new)
            elif choice == "8":
                new = input("Новая категория: ")
                current.set_category(new)
            elif choice == "9":
                new = input("Новое местоположение: ")
                current.set_location(new)
            elif choice == "10":
                new = int(input("Новый срок годности: "))
                current.set_shelflife(new)
            elif choice == "11":
                new = input("Новое айди карты: ")
                current.set_cardID(new)
            elif choice == "12":
                new = input("Новые дополнительные сведения: ")
                current.set_note(new)
            else:
                print("Неверный выбор!")
                return


        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except ProductCardError as e:
            print(f"Ошибка карты продукта: {e}")

    def write_off_current_card(self) -> None:
        """Списание текущей карточки."""

        current = self.manager.get_current_card()
        if not current:
            print("Сначала выберите карточку!")
            return

        print(f"Карточка: {current.get_name()}")
        print(f"Статус: {current.get_status()}")

        try:
            reason = input("Причина списания: ")
            current.write_off(reason)
        except (WriteOffError, InvalidReasonError) as e:
            print(f"Ошибка: {e}")

    def run(self) -> None:
        """Запуск пользовательского интерфейса."""

        is_running = True

        while is_running:
            self.print_main_menu()

            try:
                choice = input("Ваш выбор: ")
                if choice == '0':
                    is_running = False
                    print("Выход...")
                elif choice == '1':
                    self.create_card_interactive()
                elif choice == '2':
                    self.select_card_interactive()
                elif choice == '3':
                    self.manager.print_cards_list()
                elif choice == '4':
                    self.show_current_card()
                elif choice == '5':
                    self.change_current_card()
                elif choice == '6':
                    self.write_off_current_card()
                else:
                    print("Неверный выбор!")

            except KeyboardInterrupt:
                print("Выход...")
                is_running = False
            except Exception as e:
                print(f"Ошибка: {e}")
