import time

class Conta_bancaria:
    '''
    Classe que implementa métodos para manipular uma conta bancária.add().
    Atributos: titual (str), saldo (float), limite (float) e históricos (lista de dicionários).

    OBS: Operações no histórico: 0 - sacar, 1 - depositar, 2, transferir.
    '''
    
    def __init__(self, titular, saldo, limite, historico):
        '''
    Construtor da classe Conta_bancária
        '''
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico

    def depositar(self, valor):
        '''
        Método que realiza depósito na conta bancária.
        Entrada: valor (float).
        Return: True, se a operação for realizada com sucesso. False, se a operação não foi realizada.
        '''
        if valor > 0:
            self.saldo += valor
            self.historico.append({"operacao": 1,
                                   "remetente": self.titular,
                                   "destinatario": "",
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "dataetempo": int(time.time())})
            return True
        else:
            print(f"O valor {valor} é inválido!")
            return False
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({"operacao": 0,
                                   "remetente": self.titular,
                                   "destinatario": "",
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "dataetempo": int(time.time())})
            print("Saque realizado!")
        else: #sem grana em conta
            a = input(f"Deseja utilizar o Limite? (R${self.limite}) (s para sim)")
            if a == 's':
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print("Saque realizado!")
                    return True
                else:
                    print("Saldo e limite insuficientes!")    
            else:
                print("Operação com limite cancelada!")   
        return False         
                
    def exibirHistorico(self):  
        print("Histórico de Transações:")
        for transacao in self.historico:
            dt = time.localtime(transacao["dataetempo"])
            print("Op:", transacao["operacao"], #print pra aparecer na tela
                  ". Remetente:",  transacao["remetente"], 
                  ". Destinatário", transacao["destinatario"],
                  ". Saldo:", transacao["saldo"],
                  ". Valor: ", transacao["valor"],
                  ". Data e Tempo:",
                  str(dt.tm_hour) + ":" + str(dt.tm_min) + ":" + str(dt.tm_sec) + " " + str(dt.tm_mday) + ":" + str(dt.tm_mon) + ":" + str(dt.tm_year))
            
    def transferencia(self):
        