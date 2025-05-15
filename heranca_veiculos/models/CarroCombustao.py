from .Veiculos import Veiculos #o . indica que ta na mesma pasta


class CarroCombustao(Veiculos): #veiculos é a classe pai
    """
    Classe que represente um carro de combustão, herda de Veiculos
    """
    def __init__ (self, placa: str, modelo: str, marca: str,
                        ano: int, cor: str, valor_fipe: float,
                        combustivel: str, nPortas: int, nAssentos: int,
                        nCilindrada: int, nCambio: str, nivel_combustivel: int) -> None:
       
        super().__init__(placa, modelo, marca,
                        ano, cor, valor_fipe)
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindrada = nCilindrada
        self.__nCambio = nCambio
        self.__nivel_combustivel = nivel_combustivel


    def __str__(self) -> str:
        #retorna uma string com as informações do carro de combustão
    
        infos = super().__str__()#reutiliza o método __str__ da classe pai(veiculos)
        #Adiciona as informações especificas do carro a combustão
        
        infos += f"Combustivel: {self.__combustivel}\n"
        infos += f"Número de portas: {self.__nPortas}\n"
        infos += f"Número de assentos: {self.__nAssentos}\n"
        infos += f"NBumero de cilindrada: {self.__nCilindrada}\n"
        infos += f"Cambio: {self.__nCambio}\n"
        infos += f"Nivel de Combustível: {self.__nivel_combustivel}\n"
        return infos

    def abastecer(self, percentual_adicionado: int) -> bool: #tem retorno bool
        """Método para abastecer um carro a combustão
        Argumentos:
            percentual (int): percentual adicionado
        Retorno:
            bool: True se foi possivel abastecer, e Flase caso não
        """
        novo_percentual = self.__nivel_combustivel + percentual_adicionado
        if novo_percentual <= 100:
            self.__nivel_combustivel = novo_percentual
            return True
        return False