from models.Veiculos import Veiculos

class Carro(Veiculos):
    """Classe que implementa métodos específicos de carros
     Argumento: Classe pai Veiculo
     """
    def __init__(self, placa: str, modelo: str , marca: str, 
                 ano: int, cor: str):
        super().__init__(self, placa, modelo, marca, ano, cor)


    def calcular_consumo(self, distancia: float) -> float:

        if distancia > 0:
            litro_gasto = distancia/12
        else:
            litro_gasto = 0
        return litro_gasto

       
        