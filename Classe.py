class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def frear(self):
        print(f"{self.marca} {self.modelo} freando.")

    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerando.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
    
    def abrir_porta(self):
        print("Porta do carro aberta.")

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    
    def empinar(self):
        print("Moto empinando.")

Meu_veiculo = Veiculo("Toyota", "Corolla")
meu_carro = Carro("Toyota", "Corolla", "vermelho")
minha_moto = Moto("Honda", "CBR600RR", "600cc")

Meu_veiculo.frear()
Meu_veiculo.acelerar()
meu_carro.abrir_porta()
minha_moto.empinar()
