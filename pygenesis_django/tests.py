from django.test import TestCase
from .info import info


class TestInfo(TestCase):

    def test_info_text(self):
        result = ('Just use this GitHub repository as template:'
                  ' https://github.com/libresource/pygenesis-django and enjoy yourself')
        self.assertEqual(result, info())
