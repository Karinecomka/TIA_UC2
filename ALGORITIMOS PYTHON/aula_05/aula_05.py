
print("\nExercício 1 - Dias da Semana")
print()

numero = input("Digite um número de 1 a 7: ")

match numero:
    case "1":
        print("Segunda-feira")
    case "2":
        print("Terça-feira")
    case "3":
        print("Quarta-feira")
    case "4":
        print("Quinta-feira")
    case "5":
        print("Sexta-feira")
    case "6":
        print("Sábado")
    case "7":
        print("Domingo")
    case _:
        print("Dia inválido")

print("\nExercício 2 - Comandos de um Assistente")
print()

comando = input("Digite o comando: ").strip().lower()

match comando:
    case "oi" | "olá":
        print("Olá! Seja bem-vindo!")
    case "ajuda" | "?":
        print("Comandos disponíveis: oi, ajuda e sair")
    case "sair" | "0":
        print("Até breve")
    case _:
        print("Comando desconhecido")

print("\nExercício 3 - Menu de Estudos")

while True:
    print("\n=== MENU ===")
    print("1 - Mostrar uma dica sobre Python")
    print("2 - Mostrar uma dica sobre inteligência artificial")
    print("3 - Mostrar uma mensagem de incentivo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("Dica: pratique Python todos os dias.")
        case "2":
            print("Dica: sistemas de IA aprendem a partir de dados.")
        case "3":
            print("Continue estudando, você está indo muito bem!")
        case "0":
            print("Encerrando o programa.")
            break
        case _:
            print("Opção inválida.")

print("\nExercício 4 - Cadastro de Alunos")

alunos = []

while True:
    print("\n=== CADASTRO DE ALUNOS ===")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Mostrar quantidade de alunos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            nome = input("Nome do aluno: ")
            alunos.append(nome)
            print("Aluno cadastrado com sucesso.")

        case "2":
            if len(alunos) == 0:
                print("Nenhum aluno cadastrado.")
            else:
                print("Alunos cadastrados:")
                for aluno in alunos:
                    print(aluno)

        case "3":
            print("Quantidade de alunos:", len(alunos))

        case "0":
            print("Encerrando o programa.")
            break

        case _:
            print("Opção inválida.")

print("\nExercício 5 - Lista de Compras")

produtos = []

while True:
    print("\n=== LISTA DE COMPRAS ===")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Remover produto pelo nome")
    print("4 - Mostrar quantidade de produtos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            produto = input("Nome do produto: ").strip()
            if produto:
                produtos.append(produto)
                print("Produto cadastrado com sucesso.")
            else:
                print("Digite um nome válido.")

        case "2":
            if len(produtos) == 0:
                print("Nenhum produto cadastrado.")
            else:
                print("Produtos cadastrados:")
                for produto in produtos:
                    print(produto)

        case "3":
            produto = input("Digite o produto para remover: ").strip()

            if produto in produtos:
                produtos.remove(produto)
                print("Produto removido com sucesso.")
            else:
                print("Produto não encontrado.")

        case "4":
            print("Quantidade de produtos:", len(produtos))

        case "0":
            print("Encerrando o programa...")
            break

        case _:
            print("Opção inválida.")
print("\nExercício 6 -  Classificando Resultados")
resultados = ["positivo", "negativo", "positivo", "neutro", "erro", "negativo"]
positivo = 0
negativo = 0
neutro = 0
erro = 0
desconhecidos = 0
for resultado in resultados:
    match resultado:
        case "positivo":
            positivo = positivo + 1
        case "negativo":
            negativo = negativo + 1
        case "neutro":
            neutro = neutro + 1
        case "erro":
            erro = erro + 1
        case _:
            desconhecidos = desconhecidos + 1
print("Positivos:", positivo)
print("Negativos:", negativo)
print("Neutros:", neutro)
print("Erros:", erro)
print("Desconhecidos:", desconhecidos)


print("\nExercício 7 — Menu de Estatísticas")

notas = [7.5, 8.0, 5.5, 9.0, 6.5]

while True:
    print("\n=== MENU DE ESTATÍSTICAS ===")
    print("1 - Listar notas")
    print("2 - Mostrar média")
    print("3 - Mostrar maior nota")
    print("4 - Mostrar menor nota")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("\nNotas cadastradas:")
            for nota in notas:
                print(nota)

        case "2":
            media = sum(notas) / len(notas)
            print("Média das notas:", media)

        case "3":
            maior = max(notas)
            print("Maior nota:", maior)

        case "4":
            menor = min(notas)
            print("Menor nota:", menor)

        case "0":
            print("Encerrando o programa...")
            break

        case _:
            print("Opção inválida! Tente novamente.")



print("\nDesafio — Central de Análise de Previsões")

previsoes = []
while True:
    cont_cachorro = 0
    cont_gatos = 0

    print("""
        1 - Adicionar classificação
        2 - Listar classificações
        3 - Mostrar quantidade de gatos
        4 - Mostrar quantidade de cachorros
        5 - Mostrar total de classificações
        0 - Sair
    """)
    opcao = int(input("Selecione uma opção:"))
    match opcao:
        case 1:
            animal=input("Digite o animal que deseja adicionar[gato,cachorro, passaro]:").strip().lower()
            match animal:
                case "gato"|"cachorro"|"passsaro":
                    previsoes.append(animal)
                case _:
                    print("Opção invalida")
        case 2:
            if len(previsoes) == 0:
                print("A lista esta vazia")
            else:
                for previsao in previsoes:
                    print(previsao)
        case 3:
            for previsao in previsoes:
                if previsao == "gato":
                    cont_gatos += 1
            print(f"Quantidade de Gatos: {cont_gatos}")
        case 4:
            for previsao in previsoes:
                if previsao == "cachorro":
                    cont_cachorro += 1
            print(f"Quantidade de cachorros: {cont_cachorro}")
        case 5:
            if len(previsao)== 0:
                print("Lista Vazia")
            else:
                print(f"Total de classificações:{len(previsao)}")
        case 0:
            print("Saindo...")
            break
        
    
    
    

            

                    
            
            
                    

            

