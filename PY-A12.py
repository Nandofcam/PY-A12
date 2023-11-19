'''[PY-A12]Imagine que você está desenvolvendo um sistema para gerenciar uma biblioteca.
Nessa biblioteca, existem diferentes tipos de livros, como romances, biografias, livros infantis, etc.
Todos esses livros possuem algumas características em comum, como o título, o autor e a editora,
mas também possuem características específicas, como o número de páginas, a faixa etária recomendada, etc.'''

# Classe pai
class Livro:
    def __init__(self, titulo, autor, editora):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora

# Funções
    def exibir_detalhes(self):
        print("\n---- DETALHES DO LIVRO ----")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Editora: {self.editora}")

    def tipo_livro(self):
        pass

# Classe filha 1
class Romance(Livro):
    def __init__(self, titulo, autor, editora, faixa):
        super().__init__(titulo, autor, editora) # Para puxar as características da Classe pai
        self.faixa = faixa # Característica exclusiva dessa função filha
    def exibir_detalhes(self):
        super().exibir_detalhes() # Aproveitar a função da Classe pai
        print(f"Faixa etária: {self.faixa} anos") # Somente para incluir a característica da Classe filha
    def tipo_livro(self):
        print(f"Tipo do livro: Romance")

# Classe fiha 2
class Biografia(Livro):
    def __init__(self, titulo, autor, editora, pessoa):
        super().__init__(titulo, autor, editora) # Para puxar as características da Classe pai
        self.pessoa = pessoa # Característica exclusiva dessa função filha
    def exibir_detalhes(self):
        super().exibir_detalhes() # Aproveitar a função da Classe pai
        print(f"História da vida do(a): {self.pessoa}") # Somente para incluir a característica da Classe filha
    def tipo_livro(self):
        print(f"Tipo do livro: Biografia")

livro1 = Romance("Harry Potter e a Pedra Filosofal", "J. K. Rowling", "Rocco", 10)
livro2 = Biografia("A Teoria de Tudo", "Lucy Hawking", "Intrínseca", "Stephen Hawking")

livro1.exibir_detalhes()
livro1.tipo_livro()
livro2.exibir_detalhes()
livro2.tipo_livro()