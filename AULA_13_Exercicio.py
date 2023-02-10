# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Fabricante:
    def __init__(self, fabricante):
        self.fabricante = fabricante
        self.carro = None
        self.motor = None

    def inserir_motor(self, motor):
        self.carro = motor.carro
        self.motor = motor.motor

class Motor:
    def __init__(self, motor):
        self.motor = motor
        self.carro = None

    def inserir_carro(self, carro):
        self.carro = carro

    def mostrar_dois(self):
        print(self.motor, self.carro, sep='\n')

class Carro:
    def __init__(self, carro):
        self.carro = carro

    def escrever(self):
        return f'{self.carro}'

carro = Carro('Isso é um carro')
motor_rapido = Motor('Motor Rápido')
motor_rapido.carro = carro.carro

volksvagem = Fabricante('Volksvagem')
volksvagem.inserir_motor(motor_rapido)

print(volksvagem.fabricante, volksvagem.motor, volksvagem.carro, sep='\n')