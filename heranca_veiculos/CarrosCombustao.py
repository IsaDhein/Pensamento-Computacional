from .Veiculos import Veiculos

class CarrosCombustao(Veiculos):
    """
    Classe que represente um carro de combustão, herda de Veiculos
    """
    def __init__ (self, placa: str, modelo: str, marca: str,
                        ano: int, cor: str, valor_fipe: float, 
                        combustivel: str, nPortas: int, nAssentos: int,
                        nCilindrada: int, nCambio: int) -> None:
        
        super().__init__(placa, modelo, marca,
                        ano, cor, valor_fipe)
        
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindrada = nCilindrada
        self.__nCambio = nCambio

    def __str__ -> str:
        infos = super().__str__()
        infos += f"Combustivel: {self.__combustivel}\n"
        infos += f"Número de portas: {self.__nPortas}\n"
        infos += f"Número de assentos: {self.__nAssentos}\n"
        infos += f"NBumero de cilindrada: {self.__nCilindrada}\n"
        infos += f"Cambio: {self.__nCambio}\n"
        return infos
        
    