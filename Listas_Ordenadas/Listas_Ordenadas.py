from node import Node  # Importa a classe Node

class ListaOrdenada:
    def __init__(self):
        self.head = None  # Inicializa a lista vazia

    def inserir(self, valor):
        novo_no = Node(valor)  # Cria um novo nó
        if not self.head or self.head.valor >= valor:  # Se a lista está vazia ou o novo valor é menor que o primeiro
            novo_no.proximo = self.head  # O novo nó aponta para o antigo primeiro nó
            self.head = novo_no  # Atualiza a cabeça da lista
            return
        atual = self.head  # Começa pelo primeiro nó
        while atual.proximo and atual.proximo.valor < valor:  # Percorre a lista até encontrar a posição correta
            atual = atual.proximo
        novo_no.proximo = atual.proximo  # O novo nó aponta para o próximo nó na ordem
        atual.proximo = novo_no  # O nó anterior aponta para o novo nó
