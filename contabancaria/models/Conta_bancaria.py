class Conta_bancaria:
    #atributos 
    def __init__(self, titular, saldo, limite, historico):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print(f"O valor {valor} é inválido!")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({ })
            print("Saque realiazado!")
        else: #sem grana em conta
            a = input(f"Deseja utilizar o Limite? (R${self.limite}) (s para sim)")
            if a == 's':
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print("Saque realiazado!")
                else:
                    print("Saldo e limite insuficientes!")    
            else:
                print("Operação com limite cancelada!")        
                
    def transferir(self):

    def exibirHistorico(self):  

    def exibirSaldo(self):