class NoArvore:
    def __init__(self, valor):
        self.valor = valor  # Guarda o valor do nó
        self.esquerda = None  # Inicializa a subárvore esquerda como vazia
        self.direita = None  # Inicializa a subárvore direita como vazia

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None  # Inicializa a árvore vazia

    def inserir(self, valor):
        if not self.raiz:  # Se a árvore estiver vazia
            self.raiz = NoArvore(valor)  # Cria a raiz
            return
        self._inserir_recursivo(self.raiz, valor)  # Chama a função recursiva para inserir o valor

    def _inserir_recursivo(self, no, valor):
        if valor < no.valor:  # Se o valor for menor, insere na esquerda
            if no.esquerda:
                self._inserir_recursivo(no.esquerda, valor)  # Chama a recursão
            else:
                no.esquerda = NoArvore(valor)  # Cria o nó na esquerda
        else:  # Se o valor for maior ou igual, insere na direita
            if no.direita:
                self._inserir_recursivo(no.direita, valor)  # Chama a recursão
            else:
                no.direita = NoArvore(valor)  # Cria o nó na direita
