from employee import Employee


class Store:
    def __init__(self, location):
        self.__location = location
        self.__employees: list[Employee] = []
        self.__stock = []
    
    def hire_employee(self, employee):
        """Função responsável por adicionar pessoas no quadro de funcionários

        Args:
            employee (Employee | dict): Uma instância de funcionário ou um dicionário com as informações do funcionário
        """
        if isinstance(employee, dict):
            self.__employees.append(Employee(**employee))
        elif isinstance(employee, Employee):
            self.__employees.append(employee)
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
    
    
