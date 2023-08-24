#01
numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

for i, numero in enumerate(numeros):
    print(f"Posição {i+1}: {numero}")

#02
numeros = []

for i in range(10):
    numero = float(input("Digite um número real: "))
    numeros.append(numero)

numeros.reverse()

print("Números na ordem inversa:")
for numero in numeros:
    print(numero)

#03
notas = []

for i in range(4):
    nota = float(input("Digite uma nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas:")
for nota in notas:
    print(nota)

print(f"Média: {media:.2f}")

#04
idades = []

for i in range(20):
    idade = int(input("Digite uma idade: "))
    idades.append(idade)

maior_idade = max(idades)
menor_idade = min(idades)

print(f"Maior idade: {maior_idade}")
print(f"Menor idade: {menor_idade}")

#05
while idades:
    del idades[0]

print("Lista de idades vazia.")


#06
lista_de_compras = ["arroz", "feijão", "macarrão", "frutas", "produtos de limpeza", "sorvete"]

print("Lista de compras do mês:")
for item in lista_de_compras:
    print(item)

#07
if "produtos de limpeza" in lista_de_compras:
    lista_de_compras.remove("produtos de limpeza")

print("Lista de compras após remover os produtos de limpeza:")
for item in lista_de_compras:
    print(item)

#08
if "sorvete" in lista_de_compras:
    lista_de_compras.remove("sorvete")

print("Lista de compras após remover o sorvete:")
for item in lista_de_compras:
    print(item)

#09
def verificar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

numero = int(input("Digite um número: "))
paridade = verificar_paridade(numero)
print(f"O número {numero} é {paridade}.")

#10
def verificar_par_inverso(palavra1, palavra2):
    if palavra1[::-1] == palavra2:
        return True
    else:
        return False

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
resultado = verificar_par_inverso(palavra1, palavra2)
print(f"As palavras {palavra1} e {palavra2} são um par inverso: {resultado}")

#11
def verificar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

print("Números primos entre 1 e 50:")
for numero in range(1, 51):
    if verificar_primo(numero):
        print(numero)