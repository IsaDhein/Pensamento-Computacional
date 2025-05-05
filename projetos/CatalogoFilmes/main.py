#constante
capacidade = 1000
# Algoritmo para cadastrar filmes e notas

#Strings

#dicicionario
filmes = []

#Atalho para somar a média
def media(filmes):
  cnt = len(filmes)
  if cnt == 0:
    return 0
  soma = 0
  for filme in filmes:
    soma += filme["nota"]
  return soma/cnt

#duplicidade
def duplicidade(novo, filmes):
  for filme in filmes:
    if novo == filme["nome"]:
      return True
  return False

def imprime_filmes(filmes):
  for filme in filmes:
    print(f"O filme {filme['nome']} recebeu a nota {filme['nota']} da crítica!")

  for filme in filmes:
    print(f"O filme {filme['nome']} recebeu a nota {filme['nota']} da critica")

def pegarnota(filme):
    return filme["nota"]

#lista dos 3 melhores filmes
def top3(filmes):
    print("\n--- Top 3 Filmes ---")
    if len(filmes) == 0:
        print("Nenhum filme cadastrado.")
        return

    ranking = sorted(filmes, key=pegarnota, reverse=True)[:3]

    limite = 3
    if len(ranking) < 3:
        limite = len(ranking)

    posicao = 1
    for i in range(limite):
        filme = ranking[i]
        print(str(posicao) + ". " + filme["nome"] + " — Nota: " + str(filme["nota"]))
        posicao += 1

#operações
while True:
  nome = input("Digite o nome do filme ou Sair para parar o código:")
  if nome == "Sair":
    break

  #conferir se o filme não vai repetir
  if duplicidade(nome, filmes):
    print("O filme",nome, "já foi cadastrado!")
  else:
    #o replace é para caso o usuário escreva a nota com vírgula
    nota = float(input("Digite a nota do filme: ").replace("," , "."))
    filmes.append({"nome": nome, "nota":nota})
#comando para limite de 1000
if len(filmes) > capacidade:
  print("Capacidade excedida!")

#Exibindo todas as informações e a média
print(filmes)
print(f"A média das notas será: ", media(filmes))
top3(filmes)








