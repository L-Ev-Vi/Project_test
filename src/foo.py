from typing import Union

PI = 3.14


# r = float(input("Enter circle radius (int): "))
# """Запрашивает значение радиуса круга"""


def circle_area(r: float) -> Union[int, float]:
    """Функция принимает радиус круга и выводит его площадь."""
    return (PI * r) ** 2


def format_description(r: float, area: Union[int, float]) -> str:
    """Выводит строку с обозначением радиуса и площади круга"""
    return f"Radius is {str(r)}; area is {str(round(area, 2))}"


def get_information_about_the_circle(r: float) -> None:
    """Функция принимает радиус круга,
    и выводит строку с обозначением радиуса и площади круга"""
    area = circle_area(r)
    description = format_description(r, area)
    print(description)


def editing_the_list(file_path: str) -> None:
    """Принимает файл в виде списка строк, удаляет все сторонние элементы
    и обновляет файл оставляя только строки с str элементами."""
    excluded_characters = "0123456789,.:?! "
    with open(file_path, "r+", encoding="UTF-8") as file:
        files = file.read()
        name_only = "".join(letter for letter in files if letter not in excluded_characters)
        new_list = name_only.split()
        new_file = "\n".join(new_list)
    with open(file_path, "w", encoding="UTF-8") as new:
        new.write(new_file)


def editing(file_path: str) -> None:
    """Принимает файл в виде списка строк, удаляет все сторонние элементы
    и обновляет файл оставляя только строки с str элементами."""
    new_list = []
    with open(file_path, "r+", encoding="UTF-8") as file:
        files = (file.read()).split()
        for name_only in files:
            new_name = ""
            for letter in name_only:
                if letter.isalpha():
                    new_name += letter
            if new_name.isalpha():
                new_list.append(new_name)
        new_file = "\n".join(new_list)
        print(new_file)
    # with open(file_path, "w", encoding="UTF-8") as new:
    #     new.write(new_file)
