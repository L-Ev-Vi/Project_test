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


# if __name__ == "__main__":
#     get_information_about_the_circle(r)
