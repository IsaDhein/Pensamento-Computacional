class Veiculos:

#Classe com as principais funcionalidades do sistema de veiculos, como placa

    def __init__(self, placa: str, modelo: str, marca: str,
                       ano: int, cor: str, valor_fipe: float) -> None:
       
        #Construtor da classe Veiculo
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe = valor_fipe
   
    def __str__(self) -> str:
        """Retorna uma string com as informações do veiculo"""
        infos = f"Placa: {self.__placa}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Valor_fipe: {self.__valor_fipe}\n"
        return infos
   
    def getPlaca(self) -> str:
        """ Retorna a placa do veiculo"""
        return self.__placa
    
    def set_placa(self, nova_placa: str) -> None: #altera a placa do veiculo
        if self.__validar_placa(nova_placa):
            self.__placa = nova_placa
        else:
            print("Placa inválida. Siga o padrão brasileiro(3 letras e 4 números!)")


    
    #continuação

    def setValorFipe(self, valor) -> None:
        """Método que altera o valor da Fipe do Veiculo

        Argumento: valor (float): novo valor da Fipe
        Saída: True se OK
        """
        self.__valor_fipe = valor
        return True
    
    def __eq__(self, other): #other: compara veiculos
        if self.__placa == other.getPlaca():
            print("Mesmo Veículo!")
            return True
        else:
            print("Não é o mesmo veículo!")
            return False