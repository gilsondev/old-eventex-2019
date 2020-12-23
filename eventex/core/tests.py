from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self) -> None:
        self.response = self.client.get('/')

    def test_get(self) -> None:
        """GET / must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self) -> None:
        """GET / must render template index.html"""
        self.assertTemplateUsed(self.response, 'index.html')