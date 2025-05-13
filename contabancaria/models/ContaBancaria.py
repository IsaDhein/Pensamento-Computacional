import time

class ContaBancaria:
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

    def depositar(self, valor, remetente = None):
        '''
        Método que realiza depósito na conta bancária.
        Entrada: valor (float).
        Return: True, se a operação for realizada com sucesso. False, se a operação não foi realizada.
        '''
        op = 1
        # detecta se é uma transferencia
        if remetente != None:
            op = 2
        if valor > 0:
            self.saldo += valor
            self.historico.append({"operacao": op,
                                   "remetente": remetente,
                                   "destinatario": self.titular,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "dataetempo": int(time.time())})
            return True
        else:
            print(f"O valor {valor} é inválido!")
            return False
    def sacar(self, valor, destinatario = None):
        op = 0
        # detecta se é uma transferencia
        if destinatario != None:
            op = 2
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({"operacao": op,
                                   "remetente": self.titular,
                                   "destinatario": destinatario,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "dataetempo": int(time.time())})
            print("Saque realizado!")
        else: #sem dinheiro em conta
            a = input(f"Deseja utilizar o Limite? (R${self.limite}) (s para sim)")
            if a == 's':
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print("Saque realizado do limite!")
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
            print("Op:", transacao["operacao"], #print pra aparecer a lista na tela
                  ". Remetente:",  transacao["remetente"], 
                  ". Destinatário", transacao["destinatario"],
                  ". Saldo:", transacao["saldo"],
                  ". Valor: ", transacao["valor"],
                  ". Data e Tempo:",
                  str(dt.tm_hour) + ":" + str(dt.tm_min) + ":" + str(dt.tm_sec) + " " + str(dt.tm_mday) + ":" + str(dt.tm_mon) + ":" + str(dt.tm_year))
            
    def transferencia(self, destinatario, valor):
        '''
        Objetivo: método para transferir um valor entre duas contas.
        Entradas: valor(float) e obj Conta_bancaria do destinatário.
        Saída: Se ok -> True, Se NOK -> False.
        '''
        # se o saque ocorrer com sucesso
        if self.sacar(valor, destinatario.titular): #valor = o que quero mudar e destinatario.titular = pra quem quero mandar
            # deposita na conta do destinatario
            destinatario.depositar(valor, self.titular)                         