# print("Exercício 1 — Contagem Regressiva")
# print()
# numero = int(input("Digite um numero:"))
# while numero >= 0:
#     print(numero)
#     numero = numero - 1
# print()
# print("Exercício 2 — Validação de Preço")
# print()
# preco = float(input("Digite o preço do produto:"))
# while preco <= 0:
#     preco = float(input("Preço inválido. Digite novamente: "))
# print("Produto cadastrado com sucesso")
# print()
# print("Exercício 3 — Lista de Jogos")
# print()
# jogos = [
#     "Minecraft",
#     "Terraria",
#     "Stardew Valley"
# ]
# jogo4 = input("Digite o nome de um jogo:")
# jogo4.append(jogo4)

# jogo5 = input("Digite o nome de um jogo:")
# jogo4.append(jogo5)
# print("Lista Completa:",jogos)
# print("Quantidade de jogos:", len(jogos))
# print("Ultimo jogo",jogos[-1])
# print("Último jogo:", jogos[-1])


# print("\n--- EXERCÍCIO 4 — Controle de Estoque ---\n")

# produtos = []

# while True:
#     produto = input("Digite o nome do produto (ou 'fim' para encerrar): ")

#     if produto.lower() == "fim":
#         break

#     produtos.append(produto)

# print("=========== PRODUTOS CADASTRADOS ===========")

# for produto in produtos:
#     print(produto)

# print("\nQuantidade de produtos:", len(produtos))


# print("\n--- EXERCÍCIO 5 — Estatísticas de Notas ---\n")

# notas = [7.5, 8.0, 5.5, 9.0, 6.5, 10.0]

# print("Quantidade de notas:", len(notas))
# print("Soma das notas:", sum(notas))
# print("Média das notas:", sum(notas) / len(notas))
# print("Maior nota:", max(notas))
# print("Menor nota:", min(notas))


# print("\n--- EXERCÍCIO 6 — Busca em Lista ---\n")

# usuarios = [
#     "admin",
#     "maria",
#     "joao",
#     "pedro"
# ]

# usuario = input("Nome do usuário: ")
# indice = 0

# while indice < len(usuarios):
#     if usuarios[indice] == usuario:
#         print("Usuário encontrado!")
#         break

#     indice += 1

# else:
#     print("Usuário não encontrado.")


# print("\n--- EXERCÍCIO 7 — Busca de Produtos e Preços ---\n")

# produtos = []
# precos = []

# while True:
#     produto = input("Digite o nome do produto (ou 'sair' para encerrar): ")

#     if produto.lower() == "sair":
#         break

#     produtos.append(produto)

#     preco = float(input("Digite o preço: "))
#     precos.append(preco)

# print("\n========= RESUMO DOS PRODUTOS =========")

# if len(produtos) > 0:
#     print("Quantidade de produtos:", len(produtos))
#     print("Valor total da compra:", sum(precos))
#     print("Produto mais barato:", min(precos))
#     print("Produto mais caro:", max(precos))
# else:
#     print("Nenhum produto foi cadastrado.")

# print("\n--- EXERCÍCIO 8 — Sistema de Tarefas ---\n")

# tarefas = []

# while True:
#     print("1 - Adicionar tarefa")
#     print("2 - Listar tarefas")
#     print("3 - Remover tarefa")
#     print("4 - Mostrar quantidade de tarefas")
#     print("0 - Sair")

#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         tarefa = input("Digite a tarefa: ")
#         tarefas.append(tarefa)
#         print("Tarefa adicionada com sucesso!")

#     elif opcao == "2":
#         print("\n--- LISTA DE TAREFAS ---")
#         if len(tarefas) == 0:
#             print("Nenhuma tarefa cadastrada.")

#         else:
#             for tarefa in tarefas:
#                 print(tarefa)
         
#     elif opcao == "3":
#         tarefa = input("Digite a tarefa para remover: ")

#         if tarefa in tarefas:
#             tarefas.remove(tarefa)
#             print("Tarefa removida com sucesso.")
#         else:
#             print("Tarefa não encontrada.")

#     elif opcao == "4":
#         print("Quantidade de tarefas:", len(tarefas))

#     elif opcao == "0":
#         print("Sistema encerrado!")
#         break

#     else:
#         print("Opção inválida. Tente novamente.")



               




