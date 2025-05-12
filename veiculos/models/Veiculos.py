class Veiculos:
    def __init__(self, modelo, marca, placa, ano, cor, velocidade, latitude, longetude):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade
        self.latitude = latitude
        self.longetude = longetude

    def acelerar(self):
        self.velocidade += 10
        nova_latitude = self.Latitude + 1
        self.alterarLatitude(nova_latitude)
        print(f"O carro de placa {self.placa} foi acelerado até {self.velocidade} km/h")

    def frear(self):
        if(self.velocidade > 0):
            self.velocidade -= 10 
    def exibirInfo(self):
        print(f"O veiculo {self.modelo}, de placa {self.placa} está a {self.velocidade} km/h")    
        print(f"Lat: {self.latitude}, Long: {self.longetude}")

    def alterarModelo(self, modelo):
        self.modelo = modelo

    def alterarMarca(self, marca):
        self.marca = marca    


    def alterarPlaca(self, placa):
        self.placa = placa

    def alterarAno(self, ano):
        self.ano = ano

    def alterarCor(self, cor):
        self.cor = cor

    def alterarLatitude(self, latitude):
        self.latitude = latitude    

    def alterarLongetude(self, longetude):
        self.longetude = longetude   

    def obterPlaca(self):
        return self.placa     

        

      
