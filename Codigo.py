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
            sobrenome = input("Digite o sobrenome da família: "),
            numero_filhos = int(input("Digite quantos filhos você tem: ")),
            )
            os.system("cls || clear")

            lista_familia.append(familia)

            quantidade_familias += 1

            print("\nDados da família salvos com sucesso.")

            #Abrindo arquivo e certificando a escrita de dados
            with open(nome_do_arquivo, "a") as arquivo_familias:
                for integrante in lista_familia:
                    arquivo_familias.write(f"{familia.sobrenome}, {familia.numero_filhos}\n")

        case 2:
            #Lendo o arquivo
            with open(nome_do_arquivo, "r") as arquivo_de_origem:
                for linha in arquivo_de_origem:
                    sobrenome, numero_filhos = linha.strip().split(",")
                    lista_familia.append(Familia(sobrenome = sobrenome, numero_filhos = int(numero_filhos)))

            for parente in lista_familia:
                print(f"Sobrenome da família: {sobrenome}")
                print(f"Média de filhos das famílias: {sum(quantidade_de_filhos) / len(quantidade_de_filhos)}")

        case 3:
            break

        case _:
            print("Aba invalida ou inexistente. \nTente novamente.")