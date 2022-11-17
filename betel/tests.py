import unittest
from django.test import TestCase

# Create your tests here.

class TestarPaginas(TestCase):
    def testar_se_pagina_principal_carrega_completamente(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 302)
        
class TestBasic(unittest.TestCase):
    "Basic tests"

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1
