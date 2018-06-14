from django.test import Client, TestCase, override_settings

from elected_targets import models

TESTSETTINGS = {
    'DEBUG': True,
}

@override_settings(**TESTSETTINGS)
class ElectedTargetsTestCase(TestCase):

    fixtures = ['test_fixture_targets']

    def test_target_formatting(self):
        # verify that the regex formatting for target_name works
        test_targets = {
            '22466': ('Statesenatemem','CO-20'),
            '22467': ('Statesenatemem','CO-20'),
            '40362': ('Statehousemem', 'CO-2'),
            'GA_1': ('Senatemem', 'GA-1'),
            'GA_01': ('Housemem','GA-1'),
        }

        for key, value in test_targets.items():
            target = getattr(models, value[0]).objects.get(pk=key)
            self.assertEquals(target.target_name(), value[1])

