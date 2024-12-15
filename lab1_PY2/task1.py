# TODO �������� 3 ������ � ������������� � ���������� �����
import doctest

class Window:
    def __init__(self, width: float, height: float):
        """
        �������� � ���������� � ������ ������� "����"

        :param width: ������ ����
        :param height: ������ ����

        �������:
        >>> window = Window(120.0, 150.0)
        """
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("������ ���� ������ ���� ������������� ������")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("������ ���� ������ ���� ������������� ������")

        self.width = width
        self.height = height

    def open_window(self) -> None:
        """
        �������� ����.

        �������:
        >>> window = Window(120.0, 150.0)
        >>> window.open_window()
        """
        ...

    def close_window(self) -> None:
        """
        �������� ����.

        �������:
        >>> window = Window(120.0, 150.0)
        >>> window.close_window()
        """
        ...

    def resize_window(self, new_width: float, new_height: float) -> None:
        """
        ��������� �������� ����.

        :param new_width: ����� ������ ����
        :param new_height: ����� ������ ����
        :raise ValueError: ���� �������� ������������ �������

        �������:
        >>> window = Window(120.0, 150.0)
        >>> window.resize_window(140.0, 160.0)
        """
        if new_width <= 0 or new_height <= 0:
            raise ValueError("����� ������� ������ ���� �������������� �������")
        self.width = new_width
        self.height = new_height


class Facebook:
    def __init__(self, username: str, friends_count: int):
        """
        �������� � ���������� � ������ ������� "Facebook"

        :param username: ��� ������������
        :param friends_count: ���������� ������ ������������

        �������:
        >>> fb = Facebook("JohnDoe", 150)
        """
        if not isinstance(username, str) or not username:
            raise ValueError("��� ������������ ������ ���� �������")
        if not isinstance(friends_count, int) or friends_count < 0:
            raise ValueError("���������� ������ ������ ���� ��������������� ������")

        self.username = username
        self.friends_count = friends_count

    def add_friend(self) -> None:
        """
        ���������� �����.

        �������:
        >>> fb = Facebook("JohnDoe", 150)
        >>> fb.add_friend()
        """
        ...

    def remove_friend(self) -> None:
        """
        �������� �����.

        �������:
        >>> fb = Facebook("JohnDoe", 150)
        >>> fb.remove_friend()
        """
        ...

    def post_status(self, status: str) -> None:
        """
        ���������� �������.

        :param status: ����� �������

        �������:
        >>> fb = Facebook("JohnDoe", 150)
        >>> fb.post_status("Hello, world!")
        """
        ...


class Vkontakte:
    def __init__(self, username: str, groups_count: int):
        """
        �������� � ���������� � ������ ������� "���������"

        :param username: ��� ������������
        :param groups_count: ���������� �����, � ������� ������� ������������

        �������:
        >>> vk = Vkontakte("IvanIvanov", 10)
        """
        if not isinstance(username, str) or not username:
            raise ValueError("��� ������������ ������ ���� �������")
        if not isinstance(groups_count, int) or groups_count < 0:
            raise ValueError("���������� ����� ������ ���� ��������������� ������")

        self.username = username
        self.groups_count = groups_count

    def join_group(self, group_name: str) -> None:
        """
        ������������� � ������.

        :param group_name: �������� ������

        �������:
        >>> vk = Vkontakte("IvanIvanov", 10)
        >>> vk.join_group("Python Developers")
        """
        ...

    def leave_group(self, group_name: str) -> None:
        """
        ����� �� ������.

        :param group_name: �������� ������


        �������:
        >>> vk = Vkontakte("IvanIvanov", 10)
        >>> vk.leave_group("Python Developers")
        """
        ...

    def send_message(self, recipient: str, message: str) -> None:
        """
        �������� ��������� ������������.

        :param recipient: ��� ����������
        :param message: ����� ���������

        �������:
        >>> vk = Vkontakte("IvanIvanov", 10)
        >>> vk.send_message("Pavel", "������!")
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
