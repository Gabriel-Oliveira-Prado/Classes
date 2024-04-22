class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade_estoque

    def estoque_atualizado(self):
        return f'Estoque de {self.nome} atualizado. Quantidade no estoque: {self.quantidade}.'

    def calculo_preco(self):
        return f'O preço do produto {self.nome} é: {self.preco}.'

if __name__ == "__main__":
    Produto1 = Produto('borracha', 'R$ 0,50', '250')

    print(Produto1.estoque_atualizado())
    print(Produto1.calculo_preco())
