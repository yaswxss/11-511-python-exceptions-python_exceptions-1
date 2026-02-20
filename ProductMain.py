from ProductFace import (
    ProductFace,
)

def main() -> None:
    """Главная функция запуска программы."""

    print("ДОБРО ПОЖАЛОВАТЬ В СИСТЕМУ УПРАВЛЕНИЯ КАРТОЧКАМИ ТОВАРОВ")

    try:
        ui = ProductFace()
        ui.run()
    except Exception as e:
        print(f"Критическая ошибка при запуске: {e}")
        print("Программа завершена аварийно.")

if __name__ == "__main__":
    main()
