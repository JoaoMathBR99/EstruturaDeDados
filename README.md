<h1 align="center"> 
   Estruturas De Dados I
</h1>

Este repositório contém implementações de **estruturas de dados** em **Python**, incluindo Listas Encadeadas, Listas Ordenadas e Árvores Binárias. O projeto foi criado para facilitar o aprendizado prático dessas estruturas, demonstrando sua aplicação em contextos reais, como no desenvolvimento de jogos.

## Contribuidores 
###### (este trabalho foi realizado em dupla)

* João Matheus Bezerra
* RGM: 38964694

## Objetivos do Projeto

- **Aprendizado Prático:** Entender e implementar estruturas de dados fundamentais.
- **Aplicação Real:** Explorar como essas estruturas podem ser utilizadas em situações do dia a dia, como o gerenciamento de eventos em jogos.
- **Boas Práticas:** Incentivar a organização do código, modularidade e colaboração através de um repositório bem estruturado.

## Estrutura do Repositório

```
EstruturasDeDados/
├── ListasEncadeadas/
│   ├── node.py
│   └── Lista_Simples.py
├── ListasOrdenadas/
│   └── Listas_Ordenadas.py
├── ArvoresBinarias/
│   └── Arvore_Binaria.py
├── main.py
└── README.md
```

- **ListasEncadeadas:** Contém a implementação de uma lista encadeada simples.
- **ListasOrdenadas:** Contém a implementação de uma lista ordenada que insere elementos em ordem crescente.
- **ArvoresBinarias:** Contém a implementação de uma árvore binária de busca (BST).
- **main.py:** Arquivo principal que demonstra o uso de cada estrutura com exemplos práticos.
- **README.md:** Este documento, que contém a descrição do projeto, instruções de uso e orientações para contribuição.

## Pré-requisitos

- **Python 3.6+**: Certifique-se de ter uma versão recente do Python instalada.
- Recomenda-se a utilização de um ambiente virtual para isolar as dependências do projeto.

## Como Executar o Projeto

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/seu-usuario/EstruturasDeDados.git
   cd EstruturasDeDados
   ```

2. **Verifique a Estrutura de Pastas:**

   Certifique-se de que os diretórios e arquivos estão organizados conforme descrito na seção "Estrutura do Repositório".

3. **Execute o Arquivo Principal:**

   ```bash
   python main.py
   ```

   Ao executar o `main.py`, o terminal exibirá a execução dos testes para cada estrutura de dados.

## Exemplo de Saída

Ao rodar o comando `python main.py`, você deverá ver uma saída semelhante a esta:

```
====== Teste de Listas Encadeadas ======
Inserindo elementos na lista:
5 -> 10 -> 20 -> None
Removendo elemento do início: 5
10 -> 20 -> None
Resultado da busca pelo elemento 20: Node(20)

====== Teste de Listas Ordenadas ======
10 -> 20 -> 30 -> 40 -> 50 -> None

====== Teste de Árvores Binárias ======
Árvore em ordem (In-order traversal):
20 30 40 50 60 70 80
```

## Aplicações em Desenvolvimento de Jogos

- **Listas Encadeadas:** Úteis para gerenciar filas de eventos ou ações, permitindo a inserção e remoção dinâmica de elementos.
- **Listas Ordenadas:** Podem ser utilizadas para manter rankings, pontuações ou outros dados ordenados de forma eficiente.
- **Árvores Binárias:** Facilitam buscas rápidas e organizadas, sendo aplicáveis em sistemas de detecção de colisão ou organização hierárquica de objetos no jogo.

## Guia de Contribuição

Contribuições são sempre bem-vindas! Se você deseja colaborar com este projeto, siga os passos abaixo:

1. Faça um **fork** deste repositório.
2. Crie uma **branch** para sua nova funcionalidade ou correção:

   ```bash
   git checkout -b minha-nova-feature
   ```

3. Realize suas alterações e faça o **commit**:

   ```bash
   git commit -am "Descrição da alteração"
   ```

4. Envie sua branch para o repositório remoto:

   ```bash
   git push origin minha-nova-feature
   ```

5. Abra um **Pull Request** descrevendo as mudanças realizadas e o motivo delas.

Por favor, siga as boas práticas de codificação e mantenha a estrutura do projeto.

## Recursos e Leituras Complementares

- [Documentação Oficial do Python](https://docs.python.org/3/)

## Considerações Finais

Este repositório serve como base para o estudo e aplicação de estruturas de dados em Python. Esperamos que os exemplos práticos e a organização do projeto auxiliem no seu aprendizado. Fique à vontade para abrir issues, sugerir melhorias e enviar pull requests para contribuir com o aprimoramento deste projeto!
