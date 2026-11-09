print("n\Exercício 1 — Mensagem de Abertura")
print()
def mostrar_abertura():
    print("Curso de Python")
    print("Seja bem-vindo(a) ao curso!")
mostrar_abertura()
mostrar_abertura()
print("n\Exercício 2 — Mensagem de Abertura")
print()
def apresentar_aluno(nome, curso):
    print(f"A aluna {nome} esta no curso {curso}")
apresentar_aluno("Karine","Python")
print("\nExercício 3 — Calculando uma Área")
print()
def calcular_area_retangulo(base, altura):
    area = base * altura
    return area
base = float(input("Digite a base do retângulo:"))
altura = float(input("Digite a altura do retângulo:"))
resultado = calcular_area_retangulo(base, altura)
print(f"A area do retângulo é {resultado}")
print("\nExercício 5 — Calculando uma Área")
print()

def saudar(nome, saudacao="Olá"):
   mensagem = f"{saudacao},{nome}!"
   return mensagem

nome = input("Digite o seu nome: ")

print(saudar(nome))

print("\nExercício 6 — Média de uma Lista")
print()

def calcular_media(notas):
    if len(notas) == 0:
        return None

    media = sum(notas) / len(notas)
    return media


notas = [8.0, 6.0, 10.0]

resultado = calcular_media(notas)

if resultado is None:
    print("A lista de notas está vazia.")
else:
    print(f"A média das notas é {resultado}")

print("\nExercício 7 — Contando Classificações")
print()

def contar_classificacao(previsoes, categoria):
    contador = 0

    for previsao in previsoes:
        if previsao == categoria:
            contador = contador + 1

    return contador

previsoes = ["gato", "cachorro", "gato", "pássaro", "gato"]
print(contar_classificacao(previsoes, "gato"))
print(contar_classificacao(previsoes, "cachorro"))
print(contar_classificacao(previsoes, "peixe"))



print("\nDesafio — Cadastro de Alunos com Funções")
print()
def mostrar_menu():
    print("""
1 - Cadastrar aluno
2 - Listar alunos
3 - Buscar aluno
4 - Remover aluno
5 - Mostrar quantidade de alunos
0 - Sair
""")

def cadastrar_aluno(alunos,nome):
    if nome == "":
        print("Nome vazio!")
        return False
    else:
        if len(alunos) > 0:
            for aluno in alunos:
                if aluno == nome:
                    print("Este aluno ja existe")
                    return False
        else:
            alunos.append(nome)
            print("Aluno cadastrado com suecesso")
            return True
            
def listar_alunos(alunos):
    if len(alunos) == 0:
        print("lista de alunos vazia")
    else:
        for aluno in alunos:
            print(f"Nome:{aluno}")
def buscar_aluno(alunos,nome):

    for aluno in alunos:
        if aluno == nome:
            return True
    return False
def remover_aluno(alunos,nome):
    if nome in alunos:
        alunos.remove(nome)
        print("Aluno removido com sucesso")
        return True
    else:
        print("Aluno não existe")
        return False

alunos =[]

while True:
    mostrar_menu()
    op = int(input("Escolha uma opção:"))
    match op:
        case 1:
            nome = input("Digite o nome do aluno: ").strip().lower()
            cadastrar_aluno(alunos,nome)
        case 2:
            listar_alunos(alunos)
        case 3:
            nome = input("Informe o nome do aluno que deseja buscar:").strip().lower()
            if buscar_aluno(alunos,nome):
                print(f"O aluno {nome} esta devidamente matriculado!")
            else:
                print(f"O aluno {nome} não esta matriculado!")
        case 4:
            nome = input("Informe o aluno que deseja remover:")
            remover_aluno(alunos,nome)
        case 5:
            if len(alunos) == 0:
                print("Lista vazia")
            else:
                print(f"Quantidade de alunos: {len(alunos)}")
        case 0:
            print("Saindo....")
            break
        case _:
            print("Opção invalida.Tente novamente.")
        

        

            
    

            

            


















