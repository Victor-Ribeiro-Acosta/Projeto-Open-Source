class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo público
        self.idade = idade
    
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Criando um objeto da classe Pessoa
pessoa1 = Pessoa("Carlos", 30)

# Atributos
print(pessoa1.idade)
print(pessoa1.nome)

# Métodos
print(pessoa1.saudacao())