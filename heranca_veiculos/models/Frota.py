class Frota:
    def __init__(self, Veiculo):
        self.__frota = [Veiculo] #lista para armazenar as informações

    def adicionar_veiculo(self, Veiculo):
        self.__frota.append(Veiculo)

    def listar_veiculos(self):
        print(self.__frota) #lista todos os objetos dentro da lista Frota

    def consumo_total(self, distancia):
        consumo_total = 0
        for veiculo in self.__frota: #laço for pra percorrer a lista de veiculos
            consumo_total += veiculo.calcular_consumo(distancia)
        return consumo_total

    
    

        
