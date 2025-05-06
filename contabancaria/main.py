from models.Conta_bancaria import Conta_bancaria

conta = Conta_bancaria("Isabella", 1000, 10000, []) 

conta.depositar(100)
conta.sacar(50)
conta.transferir()
