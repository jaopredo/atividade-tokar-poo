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

    def test_count_by_position(self):
        """Testando função de contar quantos funcionários de um cargo tem
        """
        store1 = Store('Brasil')
        
        employees = [
            {'name': 'Diana', 'salary': 7500, 'position': 'Technician', 'cpf': '326.812.741-41'},
            {'name': 'Jack', 'salary': 5500, 'position': 'Engineer', 'cpf': '168.405.410-74'},
            {'name': 'Diana', 'salary': 7500, 'position': 'Engineer', 'cpf': '664.794.997-27'},
            {'name': 'Alice', 'salary': 9500, 'position': 'Technician', 'cpf': '507.796.968-59'},
            {'name': 'Ivy', 'salary': 5000, 'position': 'Technician', 'cpf': '124.448.392-67'},
            {'name': 'Carlos', 'salary': 3000, 'position': 'Manager', 'cpf': '481.231.422-27'},
            {'name': 'Gina', 'salary': 7500, 'position': 'Clerk', 'cpf': '459.185.884-27'},
            {'name': 'Diana', 'salary': 6500, 'position': 'Analyst', 'cpf': '272.305.809-25'},
            {'name': 'Ivy', 'salary': 9000, 'position': 'Analyst', 'cpf': '258.571.337-10'},
            {'name': 'Gina', 'salary': 9500, 'position': 'Engineer', 'cpf': '598.390.253-18'},
            {'name': 'Diana', 'salary': 6000, 'position': 'Engineer', 'cpf': '548.860.625-88'},
            {'name': 'Diana', 'salary': 5500, 'position': 'Technician', 'cpf': '222.475.341-11'},
            {'name': 'Diana', 'salary': 3500, 'position': 'Clerk', 'cpf': '273.150.899-85'},
            {'name': 'Jack', 'salary': 3000, 'position': 'Engineer', 'cpf': '790.652.796-63'},
            {'name': 'Ivy', 'salary': 4000, 'position': 'Manager', 'cpf': '111.833.866-76'},
            {'name': 'Frank', 'salary': 9500, 'position': 'Analyst', 'cpf': '826.920.916-79'},
            {'name': 'Alice', 'salary': 8000, 'position': 'Manager', 'cpf': '237.300.139-13'},
            {'name': 'Eve', 'salary': 4000, 'position': 'Analyst', 'cpf': '270.761.490-14'},
            {'name': 'Henry', 'salary': 6500, 'position': 'Manager', 'cpf': '245.817.323-74'},
            {'name': 'Frank', 'salary': 8000, 'position': 'Manager', 'cpf': '936.620.823-17'}
        ]

        for employee in employees:
            store1.hire_employee(employee)

        self.assertEqual(store1.count_employees_by_position('Engineer'), 5)
        self.assertEqual(store1.count_employees_by_position('Manager'), 5)
        self.assertEqual(store1.count_employees_by_position('Technician'), 4)
        self.assertEqual(store1.count_employees_by_position('Analyst'), 4)
        self.assertEqual(store1.count_employees_by_position('Clerk'), 2)

    def test_count_instrument_type(self):
        """Testando se está contando corretamente cada tipo de instrumento
        """
        store = Store('São Paulo')

        guitarra = Guitarra('x', 'y', 2000, 12)
        baixo = Baixo('a', 'b', 3000, 4)
        violao = Violao('c', 'd', 1500, 6)

        store.add_instrument(guitarra)
        store.add_instrument(baixo)
        store.add_instrument(violao)

        self.assertEqual(store.how_much_instruments(), { 'violao': 1, 'guitarra': 1, 'baixo': 1 })
