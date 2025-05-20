from models.Veiculos import Veiculos
from models.CarroCombustao import CarroCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConviEletrico import CarroConviEletrico
from models.Carro import Carro
from models.Moto import Moto
from models.Caminhao import Caminhao
#voyage = Veiculos("BCE9D36", "Voyage", "Volkswagen",
#2018, "Vermelho", 47793)


#jetta_gli = CarroCombustao("JDM9D36", "Jetta GLI", "Volkswagen",
#2025, "Vermelho", 250000, "Gasolina",
#4, 5, 2000, "AT 7", 24)

#tesla_model_s = CarroEletrico("JDN0A00", "Tesla Model S", "Tesla",
#2021, "Branco", 950000, 5, 4, 65, "Lítio", 491)

#fusca_eletrico = CarroConviEletrico(placa="IAA0D40", modelo="Fusca 1600 Elétrico", marca="Volkswagen",
#ano=1975, cor="Azul", valor_fipe=70000, combustivel="Gasolina",
#nCambio=4, nAssentos=5, nCilindrada=1600, nCambio= MT 4,
#nivel_combustivel=24, nivel_bateria=65, 
#tipo_bateria="Lítio", autonomia=150)

commander = Carro("UGH9J65", "Commander", "Jeep", 2015, "Preto")
yamaha = Moto("CSS7G98", "Yamaha", "Yamaha", 2018, "Vermelho")
volvo = Caminhao("JCS3H84", "Truck", "Volvo", 2020, "Branco")

#print(jetta_gli)

#if jetta_gli.abastecer(100):
#print("Abastecido com sucesso!")
#else:
#print("Erro ao abastecer!")

#print(jetta_gli)


#print(fusca_eletrico)

#fusca_eletrico.abastecer(10)

#print(fusca_eletrico)


#exercicio 1:Consumo de Combustível
distancia = float(input("Qual a distância percorrida?"))
print("Carros:")
commander.calcular_consumo(distancia)
print("Motos:")
yamaha.calcular_consumo(distancia)
print("Caminhões:")
volvo.calcular_consumo(distancia)





