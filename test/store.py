import unittest
import os
import sys
sys.path.append(os.path.join(os.getcwd()))
from store import Store
from employee import Employee


class StoreTests(unittest.TestCase):
    def test_adding_employees(self):
        """Testando se a loja adiciona os funcionários na lista corretamente
        """
        store1 = Store('Brasil')
        
        anne = Employee('Anne', '111.111.111-11', 3000, 'Gerente', store1)
        john = Employee('John', '222.222.222-22', 1500, 'Atendente', store1)

        store1.hire_employee(anne)
        store1.hire_employee({
            'name': 'John',
            'cpf': '222.222.222-22',
            'salary': 1500,
            'position': 'Atendente'
        })

        self.assertEqual(store1.employees, [anne, john])
    
    def test_adding_employees_errors(self):
        """Testando se o método de adicionar funcionários está levantando os erros que deve
        """
        store1 = Store('Brasil')
        store2 = Store('EUA')

        jubicreusa = Employee('Jubicreusa', '333.333.333-33', 7000, 'Gerente', store2)

        self.assertRaises(TypeError, store1.hire_employee, 1)
        self.assertRaises(TypeError, store1.hire_employee, 'Teste')
        self.assertRaises(TypeError, store1.hire_employee, {})
        self.assertRaises(TypeError, store1.hire_employee, jubicreusa)
    
    def test_removing_employees(self):
        """Testando se está removendo funcionários corretamente
        """
        store1 = Store('São Paulo')
        
        anne = Employee('Anne', '111.111.111-11', 3000, 'Gerente', store1)
        john = Employee('John', '222.222.222-22', 1500, 'Atendente', store1)

        store1.hire_employee(anne)
        store1.hire_employee(john)

        store2 = Store('Rio de Janeiro')
        
        jubiscreusa = Employee('Jubiscreusa', '333.333.333-33', 3000, 'Gerente', store2)
        claudia = Employee('Claudia', '444.444.444-44', 1500, 'Atendente', store2)

        store2.hire_employee(jubiscreusa)
        store2.hire_employee(claudia)

        store1.fire_employee(0)
        self.assertEqual(store1.employees, [ john ])
        store2.fire_employee('444.444.444-44')
        self.assertEqual(store2.employees, [ jubiscreusa ])
    
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
