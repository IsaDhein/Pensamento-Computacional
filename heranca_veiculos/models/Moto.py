from .Veiculos import Veiculos #não precisa ter o models porque ele ja puxa do models por estar dentro de models

class Moto(Veiculos):
    """Classe que implementa métodos específicos de carros
     Argumento: Classe pai Veiculo
     """
    def __init__(self, placa: str, modelo: str , marca: str, 
                 ano: int, cor: str):
        super().__init__(self, placa, modelo, marca, ano, cor)

   
    def calcular_consumo(self, distancia: float) -> float:
        if distancia > 0:
            litro_gasto = distancia/20
        else:
            litro_gasto = 0
        return litro_gasto