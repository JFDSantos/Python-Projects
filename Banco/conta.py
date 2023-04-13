class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
    
    def sacar(self, valor):
        self._saldo -= valor
    
    def depositar(self, valor):
        self._saldo += valor
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def saldo(self):
        return self._saldo
    

    @property
    def titular(self):
        return self._titular

    @property
    def limite(self):
        return self._limite
    