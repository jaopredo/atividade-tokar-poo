import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd()))
from store import Store
from employee import Employee
from instrument import *


class StoreTests(unittest.TestCase):
    def test_adding_employees(self):
        """Testando se a loja adiciona os funcionários na lista corretamente
        """
        store1 = Store('Brasil')
        
        john = {
            'name': 'John',
            'cpf': '222.222.222-22',
            'salary': 1500,
            'position': 'Atendente'
        }

        store1.hire_employee(john)

        self.assertEqual(store1.employees, [ Employee(store=store1, **john) ])
    
    def test_adding_employees_errors(self):
        """Testando se o método de adicionar funcionários está levantando os erros que deve
        """
        store1 = Store('Brasil')

        self.assertRaises(TypeError, store1.hire_employee, 1)
        self.assertRaises(TypeError, store1.hire_employee, 'Teste')
        self.assertRaises(TypeError, store1.hire_employee, {})
    
    def test_removing_employees(self):
        """Testando se está removendo funcionários corretamente
        """
        store1 = Store('São Paulo')
        
        anne = {
            'name': 'Anne',
            'cpf': '111.111.111-11',
            'salary': 1500,
            'position': 'Atendente'
        }
        john = {
            'name': 'John',
            'cpf': '222.222.222-22',
            'salary': 1500,
            'position': 'Atendente'
        }

        store1.hire_employee(anne)
        store1.hire_employee(john)

        store1.fire_employee(0)
        self.assertEqual(store1.employees, [ Employee(store=store1, **john) ])
        store1.fire_employee('222.222.222-22')
        self.assertEqual(store1.employees, [])
    
    def test_removing_employees_errors(self):
        """Testando se a função de remover funcionário está levantando os erros que deve
        """
        store = Store("Rio de Janeiro")

        self.assertRaises(ValueError, store.fire_employee, 1)
        self.assertRaises(ValueError, store.fire_employee, -1)
        self.assertRaises(ValueError, store.fire_employee, '444.444.444-44')
        self.assertRaises(TypeError, store.fire_employee, [])
        self.assertRaises(TypeError, store.fire_employee, {})
        self.assertRaises(TypeError, store.fire_employee, ())
        self.assertRaises(TypeError, store.fire_employee, 1.6)

    def test_adding_instruments(self):
        """Testando o método de adicionar instrumentos no estoque"""
        store = Store('São Paulo')

        guitarra = Guitarra('x', 'y', 2000, 12)
        baixo = Baixo('a', 'b', 3000, 4)
        violao = Violao('c', 'd', 1500, 6)

        store.add_instrument(guitarra)
        store.add_instrument(baixo)
        store.add_instrument(violao)

        self.assertEqual(store.stock, [ guitarra, baixo, violao ])

    def test_adding_intruments_errors(self):
        """Testando os erros do método de adicionar instrumento"""
        store = Store('São Paulo')

        with self.assertRaises(TypeError):
            store.add_instrument(1)
            store.add_instrument(1.5)
            store.add_instrument('25')

    def test_removing_instruments(self):
        """Testando o método de remover instrumento
        """
        store = Store('São Paulo')

        guitarra = Guitarra('x', 'y', 2000, 12)
        baixo = Baixo('a', 'b', 3000, 4)
        violao = Violao('c', 'd', 1500, 6)

        store.add_instrument(guitarra)
        store.add_instrument(baixo)
        store.add_instrument(violao)

        store.remove_instrument(1)

        self.assertEqual(store.stock, [ guitarra, violao ])
