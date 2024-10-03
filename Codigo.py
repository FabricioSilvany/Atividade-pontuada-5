import os
from dataclasses import dataclass

"""
Membros da equipe: 
Victor Andrade Costa Pinto
Fabrício Silvany de Jesus

Número da turma: G93313
"""

os.system("cls || clear") 

quantidade_familias = 0

salarios = []
lista_familia = []
quantidade_de_filhos = []

#Arquivo das famílias
@dataclass
class Familia:
    sobrenome: str
    numero_filhos: int
    salario: float

#Definido banco de dados
nome_do_arquivo = "pesquisa_prefeitura.txt"


#Menu
while True:
    opcao = int(input("""
          === PESQUISA DA PREFEITURA ===
    (Digite o número para acessar a aba desejada)
        
    1 || Adicionar família
    2 || Exibir resultados
    3 || Sair
    """))
    os.system("cls || clear")

    match (opcao):
        case 1:
            familia = Familia(
            sobrenome = input("Insira o sobrenome da família: "),
            numero_filhos = int(input("Insira quantos filhos você tem: ")),
            salario = float(input("Insira a sua renda mensal: ")),
            )
            os.system("cls || clear")

            lista_familia.append(familia)

            quantidade_familias += 1

            salarios.append(familia.salario)
            quantidade_de_filhos.append(familia.numero_filhos)

            media_salarial = sum(salarios) / len(salarios)
            media_filhos = sum(salarios) / len(salarios)

            #Abrindo arquivo e certificando a escrita de dados
            with open(nome_do_arquivo, "a") as arquivo_familias:
                for familiar in lista_familia:
                    arquivo_familias.write(f"Total de familias que responderam a pergunta: {quantidade_familias}\n Média salarial da população: {media_salarial:.2}\n Média de filhos da população: {media_filhos:.2}\n Maior salário: {max(salarios):.2}\n Menor Salário: {min(salarios)}\n")
            
            print("Dados salvos com sucesso.")
            
            lista_familia = []

        case 2:
            print(f"Sobrenome da família: {familia.sobrenome}")
            print(f"Número de filhos: {familia.numero_filhos}")
            print(f"Renda mensal da família: {familia.salario}")

        case 3:
            break

        case _:
            print("Aba invalida ou inexistente. \nTente novamente.")

print("=== Exibindo dados salvos ===")

print("\n=== Acessando dados de um arquivo ===")
with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        media_salarial, media_filhos, quantidade_familias, salarios = linha.strip().split(",")
        lista_familia(Familia(quantidade_familias = int(quantidade_familias), media_salarial = float(media_salarial), media_filhos = float(media_filhos), salarios = max(salarios), salarios = min(salarios) ))

print("\n ===Exibindo arquivos salvos=== ")

print(f"Quantidade de familias que responderam: {familia.quantidade_familias}")