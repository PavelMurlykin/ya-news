# news/tests/test_routes.py
# Импортируем класс HTTPStatus.
from http import HTTPStatus

from django.test import TestCase
# Импортируем функцию reverse().
from django.urls import reverse

# Импортируем класс модели новостей.
from news.models import News


class TestRoutes(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.news = News.objects.create(title='Заголовок', text='Текст')

    def test_home_page(self):
        # Вместо прямого указания адреса
        # получаем его при помощи функции reverse().
        url = reverse('news:home')
        response = self.client.get(url)
        # Проверяем, что код ответа равен статусу OK (он же 200).
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_detail_page(self):
        url = reverse('news:detail', args=(self.news.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
