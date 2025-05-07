from models.Conta_bancaria import Conta_bancaria

conta1 = Conta_bancaria("Isabella", 1000, 500, []) 
conta2 = Conta_bancaria("Pessoa2", 100, 400, [])

conta1.depositar(150)
conta1.exibirHistorico()
conta1.sacar(100)
conta1.exibirHistorico()


#transferencia
Isabella.sacar(50)
Pessoa2.depositar(50)