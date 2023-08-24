#Lista de Exercicio 16/08

#--------------------------------------------------------- Questão 01 ------------------------------------------------------------------------------------------------

dic = {'Nome':'Kleyton', 'Idade':'23 anos', 'telefone':'81818181', 'Endereço':'Rua Logos'}
print(dic['Nome'])

#--------------------------------------------------------- Questão 02 ------------------------------------------------------------------------------------------------

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
telefone = input('Digite seu telefone: ')
endere = input('Digite seu endereço: ')

dic_A = {'Nome':nome, 'Idade':idade, 'Telefone':telefone, 'Endereço':endere}
print(dic_A)

#--------------------------------------------------------- Questão 03 ------------------------------------------------------------------------------------------------

comando = "continue"
contatos = {}

while comando != "3":
    comando = input("Digite o comando: (1. Novo Contato, 2. Pesquisar Contato, 3. Sair): ")

    if comando == "1":
        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("E-mail: ").strip()
        cpf = input("CPF: ").strip()
        contatos[nome] = {
            "cpf": cpf,
            "nome": nome,
            "telefone": telefone,
            "email": email
        }
    elif comando == "2":
        nome = input("Nome: ")
        if nome in contatos:
            contato = contatos[nome]
            print(contato)
        else:
            print("Contato não encontrado")
    else:
        print("Comando inválido")

#--------------------------------------------------------- Questão 04 ------------------------------------------------------------------------------------------------

cadastro = {}  # Dicionário para armazenar todas as pessoas cadastradas
menores = {}   # Dicionário para armazenar as pessoas menores de 18 anos

# Função para cadastrar uma pessoa
def cadastrar_pessoa():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    cpf = input("Digite o CPF: ")
    pessoa = {'Nome': nome, 'Idade': idade, 'CPF': cpf}
    cadastro[cpf] = pessoa

# Cadastro de várias pessoas
quantidade = int(input("Quantas pessoas você deseja cadastrar? "))
for _ in range(quantidade):
    cadastrar_pessoa()

# Remover pessoas menores de 18 anos
for cpf, pessoa in cadastro.items():
    if pessoa['Idade'] < 18:
        menores[cpf] = pessoa

# Remover as pessoas menores de 18 anos do dicionário principal
for cpf in menores.keys():
    del cadastro[cpf]

# Exibir resultados
print("\n--- Cadastro completo ---")
for pessoa in cadastro.values():
    print(f"Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, CPF: {pessoa['CPF']}")

print("\n--- Pessoas menores de 18 anos ---")
for pessoa in menores.values():
    print(f"Nome: {pessoa['Nome']}, Idade: {pessoa['Idade']}, CPF: {pessoa['CPF']}")

#--------------------------------------------------------- Questão 05 ------------------------------------------------------------------------------------------------

dic_principal = {}
dic_backup = []

def fazer_backup():
    dic_backup.append(dic_principal.copy())

def inserir_dados():
    usuario = input("Digite seu nome de usuário: ")
    password = input("Digite seu nome de senha: ")
    email = input("Digite seu nome de email: ")
    dic_principal[usuario] = {"password": password, "email": email}

quantidade_dados = int(input("Digite a quantidade de usuários: "))
for i in range(quantidade_dados):
    inserir_dados()
    if len(dic_principal) == 5:
        print("Dicionário principal atingiu tamanho 5. Realizando backup...")
        fazer_backup()
        dic_principal.clear()

print("--- Dicionário principal ---")
for key, value in dic_principal.items():
    print(f"Usuário: {key}, Password: {value['password']}, Email: {value['email']}")

print("--- Backups realizados ---")
for i, backup in enumerate(dic_backup):
    print(f"Backup {i+1}: {backup}")

#---------------------------------------------------------------- Questão 6 -------------------------------------------------------------------------------------------

def contar_vogais():
    texto = input("Digite uma palavra: ").lower()
    vogais = ['a', 'e', 'i', 'o', 'u']
    contador = {}

    for letra in texto:
        if letra in vogais:
            if letra in contador:
                contador[letra] += 1
            else:
                contador[letra] = 1

    return contador

resultado = contar_vogais()
print(resultado)

#---------------------------------------------------------------- Questão 7 ------------------------------------------------------------------------------------------------

def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    return media

alunos = {}
nome = input("Digite o nome do aluno: ")

while nome != "":
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    alunos[nome] = [nota1, nota2]
    nome = input("Digite o nome do aluno (ou deixe em branco para encerrar): ")

print("\nMédias dos alunos:")
print("------------------")

for aluno, notas in alunos.items():
    media = calcular_media(notas)
    print(f"{aluno}: {media:.2f}")

#---------------------------------------------------------------- Questão 8 ----------------------------------------------------------------


def calcular_media_tempos(tempos):
    total = sum(tempos)
    media = total / len(tempos)
    return media

def encontrar_melhor_volta(tempos):
    melhor_volta = min(tempos)
    volta = tempos.index(melhor_volta) + 1
    return volta

def encontrar_campeao(corredores):
    campeao = min(corredores, key=corredores.get)
    return campeao

corredores = {}
num_corredores = 6
num_voltas = 10

for i in range(num_corredores):
    nome = input("Digite o nome do corredor: ")
    tempos = []
    for j in range(num_voltas):
        tempo = float(input(f"Digite o tempo da volta {j+1}: "))
        tempos.append(tempo)
    corredores[nome] = tempos

print("\nResultados:")
print("--------------")

# Encontrar a melhor volta de todos os corredores
melhor_volta = {}
for corredor, tempos in corredores.items():
    melhor_volta[corredor] = encontrar_melhor_volta(tempos)

for corredor, volta in melhor_volta.items():
    print(f"A melhor volta de {corredor} foi na volta {volta}.")

# Encontrar o campeão (menor média de tempos)
medias = {}
for corredor, tempos in corredores.items():
    media = calcular_media_tempos(tempos)
    medias[corredor] = media

classificacao = sorted(medias.items(), key=lambda x: x[1])

print("\nClassificação Final:")
print("--------------------")
posicao = 1
for corredor, media in classificacao:
    print(f"{posicao}º lugar: {corredor} - Média de tempos: {media:.2f} segundos")
    posicao += 1



