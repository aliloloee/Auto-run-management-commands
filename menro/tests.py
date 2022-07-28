from django.test import TestCase
from django.core.management import call_command

from io import StringIO

class ClosepollTest(TestCase):
    def test_command_output(self):
        out = StringIO()
        call_command('initadmin', stdout=out)
        self.assertIn('Expected output', out.getvalue())