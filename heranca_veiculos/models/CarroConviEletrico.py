from .CarroCombustao import CarroCombustao
from .CarroEletrico import CarroEletrico

class CarroConviEletrico(CarroCombustao, CarroEletrico):
    """ Classe que implementa métodos específicos de um carro convertido
    em elétrico.
    """
    def __init__(self, placa: str, modelo: str, marca: str,
                        ano: int, cor: str, valor_fipe: float,
                        combustivel: str, nPortas: int, nAssentos: int,
                        nCilindrada: int, nCambio: str, nivel_combustivel: int,
                        nivel_bateria: int, tipo_bateria: str, autonomia: int) -> None:
        CarroCombustao().__init__(self,placa, modelo, marca, ano, cor, valor_fipe, combustivel,
                         nPortas, nAssentos, nCilindrada, nCambio, nivel_combustivel)
        
        #consultor do carro elétrico
        CarroEletrico.__init__(self,placa, modelo, marca, ano, cor, valor_fipe, nAssentos, nPortas,
                               nivel_bateria, tipo_bateria, autonomia)


        #self.__nivel_bateria = nivel_bateria
        #self.__tipo_bateria = tipo_bateria
        #self.__autonomia = autonomia
    
    def __str__(self) -> str:
        infos = CarroCombustao.__str__(self)
        infos += f"Nivel de bateria: {self.__nivel_bateria.get_nivel_bateria()}\n"
        infos += f"Tipo de bateria: {self.__tipo_bateria.get_tipo_bateria()}\n"
        infos += f"Autonomia: {self.__autonomia.get_autonomia()}\n"
        return infos
    
    def abastecer(self, percentual_adicionado):
        """ Método: abastecer desativado
        Argumento:
        percentual_adicionado: float

        Returns:
        False, pois não pode abastecer.
        """
        print("Carro convertido para elétrico! Não é mais possível abastecer!")
        return False