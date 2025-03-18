from node import Node  # Importa a classe Node

class ListaSimples:
    def __init__(self):
        self.head = None  # Inicializa a lista vazia

    def inserir(self, valor):
        novo_no = Node(valor)  # Cria um novo nó
        novo_no.proximo = self.head  # O novo nó aponta para o antigo primeiro nó
        self.head = novo_no  # Atualiza o início da lista para o novo nó

    def buscar(self, valor):
        atual = self.head  # Começa do primeiro nó
        while atual:  # Percorre a lista até o final
            if atual.valor == valor:  # Se encontrar o valor, retorna True
                return True
            atual = atual.proximo  # Avança para o próximo nó
        return False  # Retorna False se não encontrar o valor

    def remover(self, valor):
        atual = self.head  # Começa do primeiro nó
        anterior = None  # Guarda o nó anterior (inicialmente nenhum)
        while atual:
            if atual.valor == valor:  # Se encontrar o valor
                if anterior:  # Se não for o primeiro nó
                    anterior.proximo = atual.proximo  # Pula o nó atual
                else:
                    self.head = atual.proximo  # Se for o primeiro nó, atualiza a cabeça da lista
                return
            anterior = atual  # Atualiza o anterior
            atual = atual.proximo  # Avança para o próximo nó
