import unittest
from unittest.mock import patch
from cadastro import *
from login import *

class MainTest(unittest.TestCase):

    @patch('builtins.input', lambda *args: 'miguel')
    def test_cadastrar_usuario(self):
        inputs = iter([
            'miguel',
            'senha'
        ])
        with patch('builtins.input', lambda *_: next(inputs)):
            usuario = cadastrando_usuario()
            self.assertEqual(usuario.login, 'ettore')
            self.assertEqual(usuario.senha, hashlib.sha256('senha'.encode()).hexdigest())


    def test_realizar_login(self):
        inputs = iter([
            'miguel',
            'login',
            'caio',

        ])
        with patch('builtins.input', lambda *_: next(inputs)):
            usuario = realizar_login()
            self.assertEqual(usuario.login, 'Miguel')
            self.assertEqual(usuario.senha, hashlib.sha256('senha'.encode()).hexdigest())
            usuario = realizar_login()
            self.assertIsNone(usuario)
            
