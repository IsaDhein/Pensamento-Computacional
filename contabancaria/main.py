from models.ContaBancaria import ContaBancaria

novaConta = [] #criação de lista

novaConta.append(ContaBancaria("Gabi", 500, 100, [])) #nova conta 
novaConta.append(ContaBancaria("Aurora", 700, 200, [])) #nova conta 
op =""

while True:

    op = input("Para ver o saldo, digite 1,\n"
               "Para realizar um saque, digite 2,\n"
               "Para realizar um depósito, digite 3,\n"
               "Para realizar uma transferência, digite 4,\n"
               "Para exibir o histórico, digite 5,\n"
               "Para excluir uma conta, digite 6,\n"
               "Para realizar um PIX, digite 7,\n"
               "Para encerrar o programa, digite sair.\n")
               
    #SALDO
    if op == "1":
    # for cliente in novaConta: #mostra o seu saldo ao titular da conta
    # print(f"Titular da conta:", cliente.titular, ", Saldo:", cliente.saldo)

        titular = input("Digite o titular da conta que deseja ver o saldo:") 

        for Conta_bancaria in novaConta: #mostra o saldo da conta do titular informado
            if Conta_bancaria.titular == titular:
                print(f"{titular} tem R${Conta_bancaria.saldo} em sua conta!")
    #SAQUE
    elif op == "2":
       
        titularSaque = input("Informe quem deseja realizar o saque:")

        valorSaque = float(input("Digite o valor do saque que você deseja realizar:"))
        for Conta_bancaria in novaConta: 
            if Conta_bancaria.titular == titularSaque:
                Conta_bancaria.sacar(valorSaque)
    #DEPÓSITO
    elif op == "3":
        
        titularDepósito = input("Informe quem deseja realizar o depósito:")

        valorDepósito = float(input("Digite o valor do depósito que você deseja realizar:"))
        for Conta_bancaria in novaConta:
            if Conta_bancaria.titular == titularDepósito:
                Conta_bancaria.depositar(valorDepósito)
        print("Depósito realizado!") 

    #TRANSFERÊNCIA
    elif op == "4":

        titularTransferencia = input("Quem deseja realizar a transferência?")

        destinatario = input("Para quem você deseja transferir o valor:")

        valorTrans = float(input("Qual o valor da transferência?"))
        for Conta_bancaria in novaConta:
            if Conta_bancaria.titular == titularTransferencia:
                for contaDestinatario in novaConta:
                    if contaDestinatario == destinatario:
                        Conta_bancaria.transferencia(contaDestinatario, valorTrans)
        print("Transferência realizada!")

    #EXIBIR HISTÓRICO
    elif op == "5":

        titularHistorico = input("Quem deseja ver o histórico? ")

        for conta in novaConta:
            if conta.titular == titularHistorico:  
                conta.exibirHistorico()           
            
    #EXCLUIR CONTA
    elif op == "6":
        
        excluirConta = input("Digite o titular da conta que deseja excluir: ")

        for conta in novaConta:
            if conta.titular == excluirConta:
                if conta.saldo > 0:
                    print(f"A conta de {excluirConta} possui um saldo de R${conta.saldo}.")
                    transferir = input("Para excluir a conta, você deve transferir o saldo restante. Deseja realizar a transferência? Aperte (S/N) para continuar ou cancelar a ação. ")
                    if transferir == "N":
                        break
                contaReceptora = input("Informe o titular da conta para transferir o saldo restante:")
                for contaTransferir in novaConta:
                    if contaTransferir.titular == contaReceptora:
                        contaTransferir.depositar(conta.saldo)
                        print(f"R${conta.saldo} transferido para {contaReceptora}!")
                        conta.saldo = 0
                        break
                novaConta.remove(conta)
                print(f"Conta de {excluirConta} excluída com sucesso!")
                break
        else:
            print("Conta não encontrada!")

    #PIX
    elif op == "7":
        remetente = input("Quem vai realizar o PIX?")

      
           

    elif op == "sair":
        break
        