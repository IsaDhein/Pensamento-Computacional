from models.Veiculos import Veiculos
from models.CarroCombustao import CarroCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConviEletrico import CarroConviEletrico
from models.Carro import Carro
from models.Moto import Moto
from models.Caminhao import Caminhao
from models.Frota import Frota
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
commander.calcular_consumo(distancia)
yamaha.calcular_consumo(distancia)
volvo.calcular_consumo(distancia)


#exercicio 2:Frota de Veiculos
gol = Carro(placa="JDM9D36",
                           modelo="Jetta GLI",
                           marca="Volkswagen",
                           ano=2025,
                           cor="Vermelho")
                           

cg_125 = Moto(placa="JDM9D36",
                           modelo="cg_125",
                           marca="Honda",
                           ano=2025,
                           cor="Amarelo")
                           

fh = Caminhao(placa="JDM9D36",
                           modelo="FH",
                           marca="Volvo",
                           ano=2025,
                           cor="Verde")

frota = Frota(gol)
frota.adicionar_veiculo(cg_125)
frota.adicionar_veiculo(fh)

print(f"{frota.consumo_total(distancia):.2f} total gasto")

print(f"{gol.calcular_consumo(distancia):.2f} Litros serão gastos a cada 12 km")
print(f"{cg_125.calcular_consumo(distancia):.2f} Litros serão gastos a cada 20 km")
print(f"{fh.calcular_consumo(distancia):.2f} Litros serão gastos a cada 5 km")

#exercicio 3:Veículo Elétrico e Sobrescrita de Métodos