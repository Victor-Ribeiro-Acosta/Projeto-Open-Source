class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def emitir_som(self):
        return "Som genérico"

# Cachorro herda de Animal
class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au!"

# Gato herda de Animal
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"

# Criando objetos
animal = Animal("Criatura")
cachorro = Cachorro("Rex")
gato = Gato("Mingau")

print(animal.emitir_som())  # Som genérico
print(cachorro.emitir_som())  # Au Au!
print(gato.emitir_som())  # Miau!