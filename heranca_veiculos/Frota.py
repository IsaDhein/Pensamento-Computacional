from models.Veiculos import Veiculos

class Frota(Veiculos):
    frota = []
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
    
    def adicionar_veiculos(self):
        Veiculos.append
        #fdkjfgndjj