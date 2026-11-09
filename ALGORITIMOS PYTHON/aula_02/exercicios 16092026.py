print ("Exercício 1 — Faixa Etária")

idade = int(input("Qual sua idade?"))


if idade <= 12:
    print("Criança")

elif idade <= 17:
    print("Adolescente")

elif idade <= 59:
    print("adulto")

else:
    print("idoso")

print("")
print ("Exercício 2 — Triângulo")
print("")

lado1 = float(input("Primeiro Lado:"))
lado2 = float(input("Segundo Lado:"))
lado3 = float(input("Terceiro lado:"))

if lado1 == lado2 and lado2 == lado3:
    print("Triângulo Equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo Isosceles")
else:
    print("Triângulo Escaleno")

print("")
print ("Exercício 3 — Desconto Progressivo")
print("")
valor_compra = float(input("Valor da Compra:"))

if valor_compra <= 100:
    desconto = 0

elif valor_compra <=300:
    desconto = 0.05

elif valor_compra <=500:
    desconto = 0.10

else:
    desconto = 0.15

valor_desconto = valor_compra * desconto
valor_final = valor_compra - valor_desconto
print("Valor original:", valor_compra)
print("Desconto:", desconto *100, "%")
print("Valor do desconto:", valor_desconto)
print("Valor Final da Compra:", valor_final)

print("")
print ("Exercício 4 — Aprovação com Frequência")
print("")
nota = float(input("Digite seu nota: "))
frequencia = float(input("Digite sua frequência:"))
if frequencia <75:
    print("Reprovado por frequência")
else:
     if nota >=7:
        print("Aprovado")
     elif nota >=5:
        print("Recuperação")
     else:
        print("Reprovado")

print("")
print ("Exercício 5 — Calculadora de IMC")
print("")
peso = float(input("Digite seu peso: "))
altura = float(input("Digite seu altura: "))
imc = peso / (altura ** 2)
if imc <18.5:
  print("Abaixo do peso")
elif imc <25:
  print("peso normal")
elif imc <30:
  print("sobrepeso")
else:
  print("Obesidade")

print("")
print ("Exercício 6 — Par ou Impar")
print("")
numero = int(input("Digite o numero:"))
if numero % 2 ==0:
    print("O numero é par.")
else:
    print("O numero é impar")

print("")
print ("Exercício 7 — Sistema de Jogo")
print("")

nivel = int(input("Digite o seu nivel:"))
espada = input("Possui espada?")
cajado = input("Possui cajado?")
if nivel >=10 and (espada  =="sim" or cajado =="sim"):
    print("Bem vindo a masmorra!")
else:
    print("Proibido sua entrada na Masmorra!")

print("")
print ("Exercício 8 — Desafio Pedra Papel e tesoura")
print("")
import random
computador = random.randint(0,2)
print("0 - Pedra")
print("1 - Papel")
print("2 - Tesoura")
jogador = int(input("Escolha uma opção(0, 1 ou 2):"))
if jogador == computador:
    print("Empate")
elif (jogador ==0 and computador ==2) or (jogador ==1 and computador ==0) or(jogador ==2 and computador ==1):
    print("Parabéns, Você ganhou!")
else:
    print("O computador ganhou!")

print("")
print ("Exercício 8 — Desafio Pedra Papel e tesoura")
print("")
usuario_correto = "admin"
senha_correta = "1234"
usuario= input("Usuario:")
senha = input("Senha:")
if usuario ==usuario_correto and senha ==senha_correta:
    print("Login realizado com sucesso!")
elif usuario !=usuario_correto:
    print("Usuario incorreto")
else:
    print("senha incorreta!")









