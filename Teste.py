import os
from dataclasses import dataclass

os.system("cls || clear")

# Estrutura de dados.
@dataclass
class Aluno:
    nome: str
    idade: int


QUANTIDADE_ALUNOS = 2

# Lista de de alunos.
lista_de_alunos = []

print("\n=== Solicitando dados dos alunos ===")
for i in range(QUANTIDADE_ALUNOS):

    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: "))
    )
    lista_de_alunos.append(aluno)

print("\n=== Exibindo dados dos alunos ===")
for aluno in lista_de_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")


# Definindo arquivo para salvar os dados.
nome_do_arquivo = "Lista_de_alunos_SENAI.txt"

# Abrindo arquivo e definindo que será feita a escrita de dados.
with open(nome_do_arquivo, "a") as arquivo_alunos:
    # Percorrendo vetor/lista.
    for aluno in lista_de_alunos:
        # Escrevendo no arquivo uma linha de cada vez.
        arquivo_alunos.write(f"{aluno.nome}, {aluno.idade}\n")

# Fechar conexão com o arquivo.
arquivo_alunos.close()
print("\n=== Dados dos alunos salvo com sucesso! ===")


# Lendo dados de um arquivo.
# Limpando a lista de alunos.
lista_de_alunos = []

print("\n=== Acessando dados de um arquivo ===")
with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        nome, idade = linha.strip().split(",")
        lista_de_alunos.append(Aluno(nome=nome, idade= int(idade)))

# Fechar conexão com o arquivo.
arquivo_alunos.close()

print("\n\n=== Exibindo dados dos alunos do arquivo ===")
for aluno in lista_de_alunos:
    print(f"Nome: {aluno.nome}")
    print(f"Idade: {aluno.idade}")
