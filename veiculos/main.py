from models.Veiculos import Veiculos

gol = Veiculos("Gol Copa", "Volkswagen", "IND-1010", 
               2006, "Amarelo", 0, 0, 0 ) 

gol.exibirInfo()
gol.acelerar()
gol.exibirInfo()
gol.frear()
gol.exibirInfo()
gol.alterarPlaca("IND1A10")
gol.exibirInfo()


