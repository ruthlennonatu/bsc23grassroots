from django.test import TestCase
from Source.grassroots import Batman


class TestBatman(TestCase):
    def test_serving_justice(self):
        batman = Batman()
        self.assertTrue(batman.serve_justice())
