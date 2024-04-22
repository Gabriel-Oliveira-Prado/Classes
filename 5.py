class Triangulo:
    def __init__(self, lado1, lado2, lado3, area, perimetro):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.area_tri = area
        self.perimetro_tri = perimetro

    def calculo_area(self):
        return f'A área do triângulo é: {self.area_tri}'

    def calculo_perimetro(self):
        return f'O perímetro do triângulo é: {self.perimetro_tri}'

if __name__ == "__main__":
    Triangulo1 = Triangulo("6", "4", "5", "40 cm", "13 cm")

    print(Triangulo1.calculo_area())
    print(Triangulo1.calculo_perimetro())
