class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo público
        self.idade = idade
    
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
