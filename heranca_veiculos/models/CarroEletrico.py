from .Veiculos import Veiculos

class CarroEletrico(Veiculos):
    """Classe que implementa métodos específicos de carros elétricos
     Argumento: Classe pai Veiculo
     """
    
    def __init__(self, placa: str, modelo: str , marca: str, 
                 ano: int, cor: str , valor_fipe: float,
                       nAssentos: int, nPortas: int,
                       nivel_bateria: int, tipo_bateria: str,
                       autonomia: int):

        Veiculos().__init__(self,placa, modelo, marca, ano, cor, valor_fipe)
        self.__nAssentos = nAssentos
        self.__nPortas = nPortas
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia
    
    def __str__(self): #imprime todas as informações
        infos = super().__str__()
        infos = f"Número de Assentos: {self.__nAssentos}\n"
        infos += f"Número de Portas: {self.__nPortas}\n"
        infos += f"Nível de Bateria: {self.__nivel_bateria}\n"
        infos += f"Tipo de Bateria: {self.__tipo_bateria}\n"
        infos += f"Autonomia: {self.__autonomia}\n"
        return infos
    
    def get_nivel_bateria(self):
        
        

        
        
