from models.Veiculos import Veiculos

class Frota(Veiculos):
 
    def __init__(self, placa: str, modelo: str , marca: str, 
                 ano: int, cor: str):

        super().__init__(self, placa, modelo, marca, ano, cor)
    def __str__(self) -> str:
           
        """Retorna uma string com as informações do veiculo"""

        infos = f"Placa: {self.__placa}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Ano: {self.__ano}\n"
        return infos
    
    
    def __init__(self):
        self.__veiculos = []  #lista privada

        #adicionar veiculos
    def adicionar_veiculo(self, veiculo: Veiculos):
        self.__veiculos.append(veiculo)

        #listar veiculos
    def listar_veiculos(self):
        print("Veículos na Frota:")
        for v in self.__veiculos:
            print(f"  - {v}")

        #calcula o consumo total
    def calcular_consumo_total(self, distancia: float) -> float:
        total = 0
        for veiculo in self.__veiculos:
            total += veiculo.calcular_consumo(distancia)
        return total

        
        