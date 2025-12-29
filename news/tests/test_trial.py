# news/tests/test_trial.py
import unittest


# Импортируем функцию для определения модели пользователя.
from django.contrib.auth import get_user_model
from django.test import Client, TestCase

# Импортируем модель, чтобы работать с ней в тестах.
from news.models import News

# Получаем модель пользователя.
User = get_user_model()

# Создаём тестовый класс с произвольным названием, наследуем его от TestCase.


class TestNews(TestCase):
    # Все нужные переменные сохраняем в атрибуты класса.
    TITLE = 'Заголовок новости'
    TEXT = 'Тестовый текст'

    # В методе класса setUpTestData создаём тестовые объекты.
    # Оборачиваем метод соответствующим декоратором.
    @classmethod
    def setUpTestData(cls):
        # Создаём пользователя.
        cls.user = User.objects.create(username='testUser')
        # Создаём объект клиента.
        cls.user_client = Client()
        # "Логинимся" в клиенте при помощи метода force_login().
        cls.user_client.force_login(cls.user)
        # Теперь через этот клиент можно отправлять запросы
        # от имени пользователя с логином "testUser".

        # Стандартным методом Django ORM create() создаём объект класса.
        # Присваиваем объект атрибуту класса: назовём его news.
        cls.news = News.objects.create(
            title=cls.TITLE,
            text=cls.TEXT,
        )

    # Проверим, что объект действительно был создан.
    @unittest.skip('')
    def test_successful_creation(self):
        # При помощи обычного ORM-метода посчитаем количество записей в базе.
        news_count = News.objects.count()
        # Сравним полученное число с единицей.
        self.assertEqual(news_count, 1)

    @unittest.skip('')
    def test_title(self):
        # Сравним свойство объекта и ожидаемое значение.
        self.assertEqual(self.news.title, self.TITLE)
