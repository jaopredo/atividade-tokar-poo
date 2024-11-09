from employee import Employee
from instrument import *


class Store:
    def __init__(self, location):
        self.location = location
        self.__employees: list[Employee] = []
        self.__stock = []
    
    def hire_employee(self, employee: dict):
        """Função responsável por adicionar pessoas no quadro de funcionários

        Args:
            employee (dict): Dicionário com as informações do funcionário
        """
        if isinstance(employee, dict):
            self.__employees.append(Employee(store=self, **employee))
        else:
            raise TypeError("Você não forneceu informações válidas sobre um funcionário")
    
    def fire_employee(self, employee: int|str):
        """Função responsável por demitir um funcionário da loja

        Args:
            employee (int | str): O ID do funcionário no quadro ou o seu CPF
        """
        if isinstance(employee, str):
            for i, emp in enumerate(self.__employees):
                if emp.cpf == employee:
                    self.__employees.pop(i)
                    break
            else:
                raise ValueError("O funcionário especificado não faz parte dessa loja")
        elif isinstance(employee, int):
            if 0 <= employee < len(self.__employees):
                self.__employees.pop(employee)
            else:
                raise ValueError("O Número passado não corresponde ao ID de nenhum funcionário")
        else:
            raise TypeError("Você não forneceu um parâmetro válido")
    
    def add_instrument(self, instrument: Instrument):
        if isinstance(instrument, Instrument):
            self.__stock.append(instrument)
        else:
            raise TypeError("Você não está passando um instrumento para ser adicionado")
    
    def remove_instrument(self, index: int):
        if isinstance(index, int) and 0 <= index < len(self.__stock):
            for i, _ in enumerate(self.__stock):
                if i == index:
                    self.__stock.pop(i)
        else:
            raise TypeError("Você passou um parâmetro inválido")

    def count_employees_by_position(self, position):
        counter = 0
        for emp in self.__employees:
            if emp.position == position:
                counter += 1
        return counter

    def how_much_instruments(self):
        infos = {
            'violao': 0,
            'guitarra': 0,
            'baixo': 0
        }

        for inst in self.__stock:
            if isinstance(inst, Violao):
                infos['violao'] += 1
            elif isinstance(inst, Guitarra):
                infos['guitarra'] += 1
            elif isinstance(inst, Baixo):
                infos['baixo'] += 1
        
        return infos

    @property
    def employees(self):
        return self.__employees
    
    @property
    def stock(self):
        return self.__stock
    
