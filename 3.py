class Conta_bancaria:
    def __init__(self,numero_conta,saldo,titular):
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.titular = titular

    def depositar(self):
        return f'Depositando na conta{self.numero_conta} e o titular {self.titular}.'
    
    def sacar(self):
        return f'O seu saldo é {self.saldo}.'
    
    def saldo_da_conta(self):
        return f'Saldo disponivel é: {self.saldo}.'
    
if __name__ == '__main__':
    saldo1 = Conta_bancaria("1900","500","Gabriel")
    print(saldo1.depositar())
    print(saldo1.sacar())
    print(saldo1.saldo_da_conta())



