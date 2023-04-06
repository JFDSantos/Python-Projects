class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def sacar(self, valor):
        self.__saldo -= valor
    
    def depositar(self, valor):
        self.__saldo += valor
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    