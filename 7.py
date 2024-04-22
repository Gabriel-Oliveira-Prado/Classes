class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def info_livro(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Número de páginas:", self.num_paginas)

    def calcular_palavras_por_pagina(self, num_palavras):
        palavras_por_pagina = num_palavras / self.num_paginas
        return palavras_por_pagina

livro_exemplo = Livro("Dom Casmurro", "Machado de Assis", 256)
livro_exemplo.info_livro()
palavras_por_pagina = livro_exemplo.calcular_palavras_por_pagina(50000)  
print("Quantidade média de palavras por página:", palavras_por_pagina)

    