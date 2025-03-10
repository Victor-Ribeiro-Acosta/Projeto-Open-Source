# Programação Orientada a Objetos (POO) em Python

<br>A Programação Orientada a Objetos (POO) é um paradigma de programação que organiza o código em torno de objetos, que são instâncias de classes. Esse paradigma busca representar conceitos do mundo real no código, facilitando a reutilização, a manutenção e a organização do software.<br><br>

## Conceitos Fundamentais
#### Classe
Um modelo para criar objetos. Define atributos (dados) e métodos (funções) que descrevem o comportamento dos objetos criados a partir dela.<br>
```
  class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo público
        self.idade = idade
    
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."
```
<br>

#### Objeto
Uma instância de uma classe, ou seja, um elemento concreto baseado no modelo definido pela classe.<br>
```
  pessoa1 = Pessoa("Carlos", 30)
  print(pessoa1.saudacao())
```
<br>

#### Atributos
Características ou propriedades do objeto.
```
  pessoa1.nome
  pessoa1.idade
```
<br>

#### Métodos
Funções que definem o comportamento do objeto, sempre possuem () no final.<br>
```
  print(pessoa1.saudacao())
```
<br>

#### Encapsulamento
Restrição do acesso direto a certos dados do objeto. Podemos restringir o acesso a certos atributos utilizando modificadores de acesso.
```
  class ContaBancaria:
      def __init__(self, titular, saldo):
          self.titular = titular
          self.__saldo = saldo  # Atributo privado
      
      def depositar(self, valor):
          self.__saldo += valor
      
      def exibir_saldo(self):
          return f"Saldo de {self.titular}: R$ {self.__saldo:.2f}"
  
  # Criando um objeto
  conta = ContaBancaria("Maria", 1000)
  conta.depositar(500)
  print(conta.exibir_saldo())
```
<br>

#### Herança
Capacidade de uma classe herdar atributos e métodos de outra classe, promovendo a reutilização de código.<br>
```
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
```
<br>

#### Polimorfismo
Capacidade de métodos terem diferentes comportamentos dependendo da classe. Isso permite que uma mesmo método seja usado para diferentes tipos de dados.
O polimorfismo permite que objetos de diferentes classes possam ser tratados de maneira uniforme. Isso significa que podemos chamar o mesmo método em diferentes classes e obter respostas adequadas ao contexto.<br>
```
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
```
<br>

#### Conclusão
A Programação Orientada a Objetos em Python permite criar códigos mais organizados, reutilizáveis e fáceis de manter. Utilizando conceitos como classes, objetos, encapsulamento, herança e polimorfismo, podemos estruturar programas de forma eficiente e intuitiva. A herança possibilita a reutilização de código, enquanto o polimorfismo garante flexibilidade ao trabalhar com diferentes classes de maneira uniforme.
