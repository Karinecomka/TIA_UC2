# print("1. Simulação de Treinamento")
# print()
# for epoca in range(1, 11):
#     print(f"Treinando época {epoca}")

# print()
# print("2. Dados de Sensores")
# print()
# temperaturas = [22.5, 24.8, 27.1, 23.9, 26.5]
# for temperatura in temperaturas:
#     print(f"Temperatura registrada: {temperatura}°C")

# print()
# print("3. Detectando Temperaturas Altas")
# print()
# temperaturas = [22, 25, 31, 28, 35, 24]
# for temperatura in temperaturas:
#     if temperatura > 30:
#         print(f"ALERTA: temperatura elevada! {temperatura}°C")
#     else:
#           print(f"Temperatura normal: {temperatura}°C")
# print()
# print("4. Classificação de Confiança")
# print()
# confiancas = [0.95, 0.65, 0.34, 0.82, 0.71]
# for confianca in confiancas:
#     if confianca >=0.8:
#         print(f"Alta confiança: {confianca}")

#     elif confianca >= 0.5:
#         print(f"Confiança média: {confianca}")
#     else:
#         print(f"Baixa confiança: {confianca}")
#  print()
# print("5. Contando Classificações")
# print()
# previsoes = [
#     "gato",
#     "cachorro",
#     "gato",
#     "pássaro",
#     "gato",
#     "cachorro"
# ]
# contador=0
# for previsao in previsoes:
#         if previsao == "gato":
#                 contador = contador + 1
        
# print(f"gatos detectados:{contador}")

# print()
# print("6. Média dos Dados")
# print()
# dados = [10, 15, 20, 25, 30]
# total=0
# for valor in dados:
#     total=total + valor
# media = total / len(dados)

# print(f"Média dos dados: {media}")

# print()
# print("7. Processamento de Texto")
# print()
# frase = input("Digite uma frase: ")

# contador = 0

# for letra in frase:
#     if letra == "a" or letra == "A":
#         contador = contador + 1
# print(f"Quantidade de letras 'a' :{contador}")

# print()
# print("8. Ignorando Dados Inválidos")
# print()

# dados = [12, 15, None, 18, None, 21]
# for valor in dados:
#     if valor is None:
#         continue
#     print(valor) 

# print()
# print("9. Analisando Previsões")
# print()          
    
# previsoes = [
#     0.92,
#     0.84,
#     0.35,
#     0.76,
#     0.28,
#     0.95
# ]
# for previsao in previsoes:
#     print(f"Previsão:{previsao}")
#     if previsao <0.30:
#         break
# print()
# print("10. Matriz de Pixels")
# print()  
# imagem = [
#     [0, 255, 0],
#     [255, 255, 0],
#     [0, 0, 255]
# ]
# for linha in imagem:
#     for pixel in linha:
#         print(pixel, end=" ")
#     print()
print()
print("11. Contador de Classes")
print()  
previsoes = [
    "gato",
    "cachorro",
    "gato",
    "gato",
    "cachorro",
    "pássaro",
    "gato"
]
gato = 0
cachorro = 0
passaro = 0

for previsao in previsoes:
    if previsao =="gato":
        gato = gato + 1
    elif previsao == "cachorro":
        cachorro = cachorro + 1
    elif previsao == "pássaro":
        passaro = passaro + 1
print(f"Gatos: {gato}")
print(f"Cachorros: {cachorro}")
print(f"Pássaros: {passaro}")

# print()
# print("12. Sistema Simples de Detecção")
# print()  

# objetos = [
#     "pessoa",
#     "carro",
#     "pessoa",
#     "bicicleta",
#     "carro",
#     "pessoa"
# ]
# pessoa = 0

# for objeto in objetos:

#     print(f"Objeto detectado: {objeto}")

#     if objeto == "pessoa":

#         pessoa = pessoa + 1

# print(f"Total de pessoas detectadas: {pessoa}")