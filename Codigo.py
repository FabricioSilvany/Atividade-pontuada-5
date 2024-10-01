import os
from dataclasses import dataclass

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
            salario = float(input("Insira a sua renda mensal: "))
            )
            os.system("cls || clear")

            lista_familia.append(familia)

            quantidade_familias += 1

            #Abrindo arquivo e certificando a escrita de dados
            with open(nome_do_arquivo, "a") as arquivo_familias:
                for integrante in lista_familia:
                    arquivo_familias.write(f"{quantidade_familias}, {familia.numero_filhos}, {familia.salario}\n")
            
            print("\nDados da família salvos com sucesso.")
            lista_familia = []

        case 2:
            salarios.append(familia.salario)
            
            print(f"{salarios}")

            #Lendo o arquivo
            with open(nome_do_arquivo, "r") as arquivo_de_origem:
                for linha in arquivo_de_origem:
                    sobrenome, numero_filhos, salario = linha.strip().split(",")
                    lista_familia.append(Familia(sobrenome = sobrenome, numero_filhos = int(numero_filhos), salario = float(salario)))

            #Fechando conexão com o arquivo
            arquivo_familias.close()

        case 3:
            break

        case _:
            print("Aba invalida ou inexistente. \nTente novamente.")