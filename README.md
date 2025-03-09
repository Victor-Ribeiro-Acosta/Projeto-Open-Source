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

