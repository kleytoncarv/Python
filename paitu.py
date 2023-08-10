#Questõe 1
NumeroReal = input("Digite um número real ")
ValorQuadrado = float(NumeroReal) * float(NumeroReal)
print(ValorQuadrado)

#Questão 2
NumeroReal = input("Digite um número real ")
QuintaParte = float(NumeroReal)/5
print(QuintaParte)

#Questão 3
NumeroInteiro = input("Digite um número inteiro ")
Sucessor = int(NumeroInteiro)+1
Antecessor = int(NumeroInteiro)-1
print("O número que antecede: ",Antecessor)
print("O número que sucede: ",Sucessor)

#Questão 4
alturaTriangulo = input("Digite a altura do triangulo: ")
baseTriangulo = input("Digite a base do triangulo: ")
areaTriangulo = (float(baseTriangulo) * float(alturaTriangulo))/2
print("A área do Triangulo é: ", areaTriangulo)

#Questão 5
NumeroN = float(input("Digite um número: "))
if NumeroN > 0:
    print("Positivo")
elif NumeroN < 0:
    print("Negativo")
else:
    print("Nulo")

#Questão 6
Multiplo = float(input("Digite um número (Multiplo): "))
CalcMultiplo = (Multiplo%3)

if CalcMultiplo == 0:
    print("Multiplo de 3")
else:
    print("Não é multiplo de 3")

#Questão 7
NumeroD = float(input("Digite um numero (Divisor): "))
if (NumeroD % 5) == 0:
    print("Divisível por 5")
else:
    print("Não é divisível por 5")

#Questão 8
NumeroA = float(input("Digite o primeiro número: "))
NumeroB = float(input("Digite o segundo número: "))
if NumeroB == 0:
    print("Não é possível dividir por zero")
elif NumeroA%NumeroB == 0:
    print(NumeroA,"é divisível por",NumeroB)
else:
    print("Não é possível dividir!")

#Questao9
print("Questao9")
altura = float(input("Digite a sua altura: "))
sexo = input("Você é do sexo [1]Masculino ou [2]Feminino?")

if sexo == "1":
    pesoideal=72.7*altura-58
    print("Seu peso ideal é {}".format(pesoideal))
elif sexo == "2":
    pesoideal=62.1*altura-44.7
    print("Seu peso ideal é {}".format(pesoideal))

print()
#Questao10
print("Questao10")
A = int(input("Digite o primeiro numero: "))
B = int(input("Digite o segundo numero: "))
C = int(input("Digite o terceiro numero: "))
lista = [A,B,C]
lista.sort()
print(lista)

print()
#Questao11
print("Questao11")
A1 = int(input("Digite o primeiro numero: "))
B1 = int(input("Digite o segundo numero: "))
C1 = int(input("Digite o terceiro numero: "))
lista = [A1,B1,C1]
lista.sort()
lista.reverse()
print(lista)


print()
#Questao12
print("Questao12")
soma = 0
for i in range(0,501):
    if i % 2 == 0:
        soma += i

print(soma)


print()
#Questao13
print("Questao13")
listaAltura = [1.1]
h = 1.2

while len(listaAltura) < 51:
    h = h + 0.1
    listaAltura.append(h)

listaAltura.sort()

print(listaAltura)
print('A menor altura da lista é {}, e a maior altura é {}'.format(listaAltura[0], listaAltura[-1]))

print()
#Questao14
print("Questao14")
listaPeso = [20]
p = 30

while len(listaPeso) < 91:
    p = p + 1
    listaPeso.append(p)
listaPeso.sort()
print(listaPeso)
print('O boi mais gordo é {}, e o mais magro é {}'.format(listaPeso[-1], listaPeso[0]))

# # Uma pesquisa sobre algumas características físicas da população de uma determinada região coletou os seguintes dados, referentes a
# cada habitante, para serem analisados:
# • Sexo (masculino, feminino)
# • Cor dos olhos (azuis, verdes, castanhos)
# • Cor dos cabelos (louros, castanhos, pretos)
# • Idade
# Fazer um algoritmo que determine e escreva:
# a) A maior idade dos habitantes.
# b) A porcentagem de indivíduos do sexo feminino cuja idade entre 18 e 35 anos inclusive e que tenham olhos verdes e cabelos louros.

def linha():
    print ('----------------')

def caract():
    sexo = input('informe seu sexo? ')
    olhos = input('informe a cor do seu olhor? ')
    cabelo = input('informe a cor do seu cabelo? ')
    idade = int(input("Digite sua idade: "))
    if idade > idade:
        print ('o individuo de maior idade e: ', idade)
    if sexo == 'feminino' and olhos =='verdes' and cabelo == 'louro' and idade >= 18 and idade <= 35:
        porce = 1
        print('Quantidade de individuos: ', (porce*100)/100)
        
caract()
linha()

# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por código. Os dados utilizados para a
# contagem obedecem à seguinte codificação:
# • 1, 2, 3, 4 = voto para os respectivos candidatos;
# • 5 = voto nulo;
# • 6 = voto em branco.
# Elabore um algoritmo que calcule e escreva:
# a) O total de votos para cada candidato e seu percentual sobre o total;
# b) O total de votos nulos e seu percentual sobre o total;
# c) O total de votos em branco e seu percentual sobre o total.
# Como finalizador do conjunto de votos, tem-se o valor 0.


def eleicao(voto):
    total = 0
voto = int(input('Informe o seu voto: '))
if voto == 1:
    total+=(total*100)/100
    return voto,"voto no 1", total
elif voto == 2:
          total+= (total*100)/100
          return voto,"voto no 2", total
      elif voto == 3:
          total+= (total*100)/100
          return voto,"voto no 3", total
      elif voto == 4:
          total+= (total*100)/100
          return voto,"voto no 4", total
      elif voto == 5:
          total+= (total*100)/100
          return voto,"voto nulo", total
      elif voto == 6:
          total+= (total*100)/100
          return voto,"voto em branco", total
      
      
      
for i in range(1,6):   
  print(eleicao(2))

print("---------------------------------------")
print("Questão 18")
lista = [5.0, 4.9, 7.8, 10.0]
print(lista)
mem0 = lista[0]
mem1 = lista[1]
mem2 = lista[2]
mem3 = lista[3]

media = (mem0 + mem1 + mem2 + mem3) / 4
print(media)
print(min(lista))
print(max(lista))

print("---------------------------------------")
print("Questão 19")

if media >= 7:
    print("APROVADO")
if media <= 7:
    media = mem3 / 4
if media >= 5:
    print("APROVADO")
else:
    print("REPROVADO", media)

print("---------------------------------------")
print("Questão 20")
frase = ("exercícios de java")
print("exercicios de java")
exe = (input("digite a palavra 'python':\n "))
print("exercícios de ",exe)

print("---------------------------------------")
print("Questão 21")
string = ("exercícios de python")
string = string.upper()
print(string)

print("---------------------------------------")
print("Questão 22")

string2 = "nós estamos aqui presentes"
usu = (input("Digite o caractere que deseja saber a quantidade:\n"))
string2 = string2.count(usu)
print(string2)

#Questão 27
def eh_par_inverso(palavra1, palavra2):
    return palavra1 == palavra2[::-1]

def encontrar_pares_inversos(lista_palavras):
    pares_inversos = []
    for i in range(len(lista_palavras)):
        for j in range(i+1, len(lista_palavras)):
            palavra1 = lista_palavras[i]
            palavra2 = lista_palavras[j]
            if eh_par_inverso(palavra1, palavra2):
                pares_inversos.append((palavra1, palavra2))
    return pares_inversos

palavras = ["sopa", "apos", "ola", "alo", "python", "nohtyp"]

pares = encontrar_pares_inversos(palavras)
print("Pares inversos encontrados:")
for par in pares:
    print(par[0], "-", par[1])

#Questão 28
numeros = list(range(11))

numeros_impares = [num for num in numeros if num % 2 != 0]

print("Lista de números ímpares:")
print(numeros_impares)

#Questão 29
numeros = []
for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

primeiro_numero = numeros[0]

numeros_maiores = [num for num in numeros if num >= primeiro_numero]
numeros_menores = [num for num in numeros if num < primeiro_numero]

lista_ordenada = numeros_menores + numeros_maiores
print("Lista de números ordenados:")
print(lista_ordenada)

#Questão 30
numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))
numero4 = int(input("Digite o quarto numero: "))
numero5 = int(input("Digite o quinto numero: "))

lista = [numero1, numero2, numero3, numero4, numero5]
print(sorted(lista))

#Questão 31
def contar_caractere(string, caractere):
    contador = 0
    for char in string:
        if char == caractere:
            contador += 1
    return contador

string = input("Digite uma string: ")
caractere = input("Digite um caractere: ")

ocorrencias = contar_caractere(string, caractere)
print(f"O caractere '{caractere}' ocorre {ocorrencias} vezes na string '{string}'.")
