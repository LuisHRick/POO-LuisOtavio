class Carro:
    def __init__(self, carro) -> None:
        self.nome = carro
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, nome):
        self._motor = nome

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome

class Motor:
    def __init__(self, motor) -> None:
        self.nome = motor

class Fabricante:
    def __init__(self, fabricante) -> None:
        self.nome = fabricante



fusca = Carro('Fusca')
volkswagem = Fabricante('Volkswagem')
fusca.fabricante = volkswagem
motor = Motor('1.0')
fusca.motor = motor
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = volkswagem
gol.motor = motor
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)