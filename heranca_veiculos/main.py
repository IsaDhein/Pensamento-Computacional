from models.Veiculos import Veiculos
from models.CarroCombustao import CarroCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConviEletrico import CarroConviEletrico
from models.Carro import Carro
from models.Moto import Moto
from models.Caminhao import Caminhao
from models.Frota import Frota
from models.VeiculoEletrico import VeiculoEletrico
from utils.erros import * # * tudo que ta dentro da pasta vai ser importado
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

byd = VeiculoEletrico(placa="JDN0A00",
                              modelo="BYD",
                              marca="BYD",
                              ano=2021,
                              cor="Rosa",
                              valor_fipe=950000,
                              nivel_bateria=65)

frota = Frota(gol)
frota.adicionar_veiculo(cg_125)
frota.adicionar_veiculo(fh)

print(f"{frota.consumo_total(distancia):.2f} total gasto")

print(f"{gol.calcular_consumo(distancia):.2f} Litros serão gastos a cada 12 km")
print(f"{cg_125.calcular_consumo(distancia):.2f} Litros serão gastos a cada 20 km")
print(f"{fh.calcular_consumo(distancia):.2f} Litros serão gastos a cada 5 km")
print(f"{byd.calcular_consumo(distancia):.2f} de KWh gasta a cada 0.15 km")

#exercicio 3:Veículo Elétrico e Sobrescrita de Métodos
print(f"{byd.calcular_consumo(distancia):.2f} de KWh gasta a cada 0.15 km")

byd.recarregar(100)

frota = Frota(gol)
frota.adicionar_veiculo(cg_125)
frota.adicionar_veiculo(fh)
frota.adicionar_veiculo(byd)

print(f"{frota.consumo_frota(distancia):.2f}")

veiculos = [
    Carro(placa="ABC1234", modelo="Gol", marca="Volkswagen", ano=2020, cor="Prata", valor_fipe=50000),
    Moto(placa="XYZ5678", modelo="CG 160", marca="Honda", ano=2021, cor="Preto", valor_fipe=12000),
    VeiculoEletrico(placa="ABC1234", modelo="Leaf", marca="Nissan", ano=2022, cor="Branco", valor_fipe=150000, nivel_bateria=80),
    Caminhao(placa="XYZ5678", modelo="FH", marca="Volvo", ano=2019, cor="Azul", valor_fipe=300000)
]

print(fh == byd)

#Identica veiculos duplicados a partir da placa
duplicados = []
for i in range(len(veiculos)):
    for j in range(i + 1, len(veiculos)):
        if veiculos[i] == veiculos[j]:
            duplicados.append((veiculos[i], veiculos[j]))

#Exibe os veículos duplicados
print("\nVeículos duplicados encontrados:")
for v1, v2 in duplicados: #veiculos duplicados
    print(f"Duplicado: {v1} e {v2}")


#Exercicio 1:Entrada de Dados e Consumo(powerpoint 20/05)
#toda tratativa de erro, fazer no main
try: #tratação de erros
    distancia = float(input("Digite a distancia:"))
    if distancia < 0:
        raise DistanciaNegativa("Distância negativa não é permitida!")
except ValueError as erro:
    print(f"Erro: {erro}")
except DistanciaNegativa as erro:
    print(f"Erro: {erro}")


try:
    placa = input("Informe a placa do seu veículo:")#verifica se a placa é válida
    if placa[:3].isalpha() and placa[3:4].isnumeric() and placa[4:5].isalpha() and placa[5:].isnumeric(): #5: conferi ate o fim
        raise PlacaInvalida("Placa inválida! Siga o padrão brasileiro Mercosul(LLLNLNN)")
except PlacaInvalida as erro:
    print(f"Erro: {erro}")


try: 
    for Veiculo in Frota:
        if not Veiculo:
            raise ListaVazia("Nenhum veículo na lista!")
        consumo = Veiculo.calcular_consumo(distancia)
        print(f"Veículo {Veiculo.get_placa}), Consumo: {consumo:.2f} litros")
except ValueError as erro:
    print(f"Erro: {erro}")
except DistanciaNegativa as erro:
    print(f"Erro: {erro}")
except ListaVazia as erro:
    print(f"Erro: {erro}")






    