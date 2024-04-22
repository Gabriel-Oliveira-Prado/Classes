class Animal:
    def __init__(self, nome, idade, especie):
        self.nome = nome
        self.idade = idade
        self.especie = especie

    def emitir_som(self):
        pass

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Espécie: {self.especie}")
        self.emitir_som()

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade, "Cachorro")

    def emitir_som(self):
        print("au au!")
        
cachorro1 = Cachorro('Totó',"7 anos")
cachorro1.mostrar_informacoes()