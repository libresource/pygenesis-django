from django.test import TestCase, Client
from django.core.management import call_command
from django.apps import apps
from django.conf import settings
from .info import info

class TestInfo(TestCase):
    def setUp(self):
        self.client = Client()

    def test_info_text(self):
        result = ('Just use this GitHub repository as template:'
                 ' https://github.com/libresource/pygenesis-django and enjoy yourself')
        self.assertEqual(result, info())

    def test_django_configuration(self):
        """Test that Django is properly configured"""
        self.assertTrue(apps.is_installed('pygenesis_django'))

        self.assertIn('django.contrib.admin', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.auth', settings.INSTALLED_APPS)
        self.assertIn('django.contrib.contenttypes', settings.INSTALLED_APPS)

        try:
            call_command('check')
        except Exception as e:
            self.fail(f"Django management command failed: {str(e)}")

    def test_database_connection(self):
        """Test that we can connect to the database"""
        from django.db import connection
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT 1')
        except Exception as e:
            self.fail(f"Database connection failed: {str(e)}")