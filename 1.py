class Carro:
    def __init__(self, marca, cor, modelo, ano) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.ligado = False  

    def __str__(self):
        estado = "ligado" if self.ligado else "desligado"
        return f'''Marca: {self.marca} 
        Modelo: {self.modelo} 
        Cor: {self.cor} 
        Ano: {self.ano}
        Estado: {estado}
'''

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(f'O seu {self.marca} ligou.')
        else:
            print(f'O seu {self.marca} já está ligado.')

    def desligar(self):
        if self.ligado:
            self.ligado = False
            print(f'O seu {self.marca} desligou!')
        else:
            print(f'O seu {self.marca} já está desligado.')

    def acelerar(self):
        if self.ligado:
            print(f'O seu {self.marca} está acelerando.')
        else:
            print(f'Não é possível acelerar. Por favor, ligue o {self.marca} primeiro.')


meu_carro = Carro(marca="Honda", cor="Azul", modelo="civic", ano=2007)
print(meu_carro)  
meu_carro.ligar()  
meu_carro.acelerar()    
meu_carro.desligar() 