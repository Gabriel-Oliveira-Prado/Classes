class Pedido:
    def __init__(self):
        self.itens = []
        self.total = 0.0
        self.status = "Pendente"

    def adicionar_item(self, item, preco):
        self.itens.append((item, preco))
        self.total += preco

    def calcular_total(self):
        return self.total

    def alterar_status(self, novo_status):
        self.status = novo_status

pedido_exemplo = Pedido()
pedido_exemplo.adicionar_item("Hambúrguer", 10.99)
pedido_exemplo.adicionar_item("Batatas Fritas", 4.50)
pedido_exemplo.adicionar_item("Refrigerante", 2.50)

print("Itens do pedido:")
for item, preco in pedido_exemplo.itens:
    print(f"{item}: R${preco:.2f}")

print("Total a ser pago:", pedido_exemplo.calcular_total())
print("Status do pedido:", pedido_exemplo.status)

pedido_exemplo.alterar_status("Em preparo")
print("Novo status do pedido:", pedido_exemplo.status)

