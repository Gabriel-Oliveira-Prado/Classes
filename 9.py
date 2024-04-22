class Alunos:
    def __init__(self, nome, idade, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    def calcular_media(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        return media

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media >= 6:
            return 'Aprovado'
        else:
            return 'Reprovado'

if __name__ == '__main__':
    aluno1 = Alunos('Carlos', 18, 6, 6, 8, 7)
    print(aluno1.verificar_aprovacao())