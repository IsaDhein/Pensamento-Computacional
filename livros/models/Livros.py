#criando a classe livro
class Livros:
    def __init__(self, titulo, autor, ano_publicacao, numero_paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__ano_publicacao = ano_publicacao
        self.__numero_paginas = numero_paginas
        self.__pagina_atual = 1


    def avancarPagina(self):
      if self.__pagina_atual < self.__numero_paginas:
        self.__pagina_atual += 1
      else:
        print("Você já está na última página.")

    def voltarPagina(self):
      if self.__pagina_atual > 1:
          self.__pagina_atual -= 1
      else:
        print("Você já está na última página.")

    def exibirInformacoes(self):
      print(f"Título: {self.__titulo}")
      print(f"Autor: {self.__autor}")
      print(f"Ano de publicação: {self.__ano_publicacao}")
      print(f"Número total de páginas: {self.__numero_paginas}")
      print(f"Página atual: {self.__pagina_atual}")