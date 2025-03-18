class Node: #Define uma classe chamada Node
            #Cada nó contém um valor (item) e uma referência para o próximo nó.
    def __init__(self, valor): #Construtor da classe
        self.valor = valor #Atributo que armazena o valor do nó
        self.proximo = None #Inicializa o ponteiro proximo como None
