class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return f"Depósito de R$ {valor:.2f} realizado."
        return "Valor inválido."
    
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            return f"Saque de R$ {valor:.2f} realizado."
        return "Saldo insuficiente ou valor inválido."
    
    def exibir_saldo(self):
        return f"Saldo de {self.titular}: R$ {self.__saldo:.2f}"

# Criando um objeto da classe ContaBancaria
conta = ContaBancaria("Maria", 1000)
print(conta.exibir_saldo())
print(conta.depositar(500))
print(conta.sacar(300))
print(conta.exibir_saldo())