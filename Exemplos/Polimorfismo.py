class Veiculo:
    def mover(self):
        return "O veículo está se movendo."

class Carro(Veiculo):
    def mover(self):
        return "O carro está andando na estrada."

class Barco(Veiculo):
    def mover(self):
        return "O barco está navegando na água."

class Aviao(Veiculo):
    def mover(self):
        return "O avião está voando no céu."

# Função que usa polimorfismo

def deslocar(veiculo):
    print(veiculo.mover())

# Criando objetos das subclasses
meu_carro = Carro()
meu_barco = Barco()
meu_aviao = Aviao()

# Chamando a função polimórfica
for veiculo in [meu_carro, meu_barco, meu_aviao]:
    deslocar(veiculo)