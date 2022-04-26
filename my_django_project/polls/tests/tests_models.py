from django.test import TestCase
from ..models import *


class UnitTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('setUpTestData: Hello,admin')
        pass

    def setUp(self):
        print('setUp: Test method')
        pass

    def test_is_false(self):
        print('Method: isFalse complied')
        self.assertFalse(False)

    def test_is_add(self):
        print('Method: is_add_method compiled')
        self.assertEqual(5+5,10)

    def test_is_multiple(self):
        print('Method: is_multiple_method compiled')
        self.assertEqual(5 * 5, 25)
