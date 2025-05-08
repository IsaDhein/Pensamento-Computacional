from models.Conta_bancaria import Conta_bancaria

novaConta = [] # criação de lista

novaConta.append(Conta_bancaria("Gabi", 500, 100, [])) # nova conta 
novaConta.append(Conta_bancaria("Aurora", 700, 200, [])) # nova conta 

for Conta_bancaria in novaConta: # mostra o seu saldo ao titular da conta
    print(f"Titular da conta:", Conta_bancaria.titular, ", Saldo:", Conta_bancaria.saldo)

titular = input("Digite o titular da conta que deseja ver o saldo:") 

for Conta_bancaria in novaConta: # mostra o saldo da conta do titular informado
    if Conta_bancaria.titular == titular:
        print(f"{titular} tem R$ {Conta_bancaria.saldo} em sua conta!")

titularSaque = input("Informe quem deseja realizar o saque:")
\
valorSaque = float(input("Digite o valor do saque que você deseja realizar:"))
for Conta_bancaria in novaConta: 
    if Conta_bancaria == titularSaque:
        Conta_bancaria.sacar(valorSaque)
print("Saque realizado!")
      