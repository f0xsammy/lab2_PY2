# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Window:
    def __init__(self, width: float, height: float):
        """
        Создание и подготовка к работе объекта "Окно"

        :param width: Ширина окна
        :param height: Высота окна

        Примеры:
        >>> window = Window(120.0, 150.0)
        """
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина окна должна быть положительным числом")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота окна должна быть положительным числом")

        self.width = width
        self.height = height

    def open_window(self) -> None:
        """
        Открытие окна.

        Примеры:
        >>> window = Window(120.0, 150.0)
        >>> window.open_window()
        """
        ...

    def close_window(self) -> None:
        """
        Закрытие окна.

        Примеры:
        >>> window = Window(120.0, 150.0)
        >>> window.close_window()
        """
        ...

    def resize_window(self, new_width: float, new_height: float) -> None:
        """
        Изменение размеров окна.

        :param new_width: Новая ширина окна
        :param new_height: Новая высота окна
        :raise ValueError: Если переданы некорректные размеры

        Примеры:
        >>> window = Window(120.0, 150.0)
        >>> window.resize_window(140.0, 160.0)
        """
        if new_width <= 0 or new_height <= 0:
            raise ValueError("Новые размеры должны быть положительными числами")
        self.width = new_width
        self.height = new_height


class Facebook:
    def __init__(self, username: str, friends_count: int):
        """
        Создание и подготовка к работе объекта "Facebook"

        :param username: Имя пользователя
        :param friends_count: Количество друзей пользователя

        Примеры:
        >>> fb = Facebook("JohnDoe", 150)
        """
        if not isinstance(username, str) or not username:
            raise ValueError("Имя пользователя должно быть строкой")
        if not isinstance(friends_count, int) or friends_count < 0:
            raise ValueError("Количество друзей должно быть неотрицательным числом")

        self.username = username
        self.friends_count = friends_count

    def add_friend(self) -> None:
        """
        Добавление друга.

        Примеры:
        >>> fb = Facebook("JohnDoe", 150)
        >>> fb.add_friend()
        """
        ...

    def remove_friend(self) -> None:
        """
        Удаление друга.

        Примеры:
        >>> fb = Facebook("JohnDoe", 150)
        >>> fb.remove_friend()
        """
        ...

    def post_status(self, status: str) -> None:
        """
        Публикация статуса.

        :param status: Текст статуса

        Примеры:
        >>> fb = Facebook("JohnDoe", 150)
        >>> fb.post_status("Hello, world!")
        """
        ...


class Vkontakte:
    def __init__(self, username: str, groups_count: int):
        """
        Создание и подготовка к работе объекта "ВКонтакте"

        :param username: Имя пользователя
        :param groups_count: Количество групп, в которых состоит пользователь

        Примеры:
        >>> vk = Vkontakte("IvanIvanov", 10)
        """
        if not isinstance(username, str) or not username:
            raise ValueError("Имя пользователя должно быть строкой")
        if not isinstance(groups_count, int) or groups_count < 0:
            raise ValueError("Количество групп должно быть неотрицательным числом")

        self.username = username
        self.groups_count = groups_count

    def join_group(self, group_name: str) -> None:
        """
        Присоединение к группе.

        :param group_name: Название группы

        Примеры:
        >>> vk = Vkontakte("IvanIvanov", 10)
        >>> vk.join_group("Python Developers")
        """
        ...

    def leave_group(self, group_name: str) -> None:
        """
        Выход из группы.

        :param group_name: Название группы


        Примеры:
        >>> vk = Vkontakte("IvanIvanov", 10)
        >>> vk.leave_group("Python Developers")
        """
        ...

    def send_message(self, recipient: str, message: str) -> None:
        """
        Отправка сообщения пользователю.

        :param recipient: Имя получателя
        :param message: Текст сообщения

        Примеры:
        >>> vk = Vkontakte("IvanIvanov", 10)
        >>> vk.send_message("Pavel", "Привет!")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
