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
    numero_fiilhos: int


#Definido banco de dados
nome_do_arquivo = "pesquisa_prefeitura.txt"

#Abrindo arquivo e certificando a escrita de dados
with open(nome_do_arquivo, "a") as arquivo_familias:
    for familia in lista_familia:
        arquivo_familias.write(f"{familia.numero_filhos, {familia.sobrenome}}")

#Acessando dados do arquivo:
with open(nome_do_arquivo, "r") as arquivo_de_origem:
    for linha in arquivo_de_origem:
        sobrenome, numero_filhos = linha.strip().split(",")
        lista_familia.append(Familia(sobrenome = sobrenome, numero_filhos = int(numero_filhos)))

#Fechando conexão com o arquivo
arquivo_familias.close()

#Menu
while True:
    opcao = input(print("""
    === PESQUISA DA PREFEITURA ===
    (Digite o número para acessar a aba desejada)
        
    1 || Adicionar família
    2 || Exibir resultados
    3 || Sair

   :
    """))

    match (opcao):
        case 1:
            familia = Familia(
            sobrenome = input("Digite o sobrenome da família: "),
            numero_fiilhos = int(input("Digite quantos filhos você tem: "))
            )
            lista_familia.append(familia)

            quantidade_familias += 1

            print("Dados da família salvos com sucesso.")
            #Fechando conexão com o arquivo
            arquivo_familias.close()

        case 2:
            for parente in lista_familia:
                print(f"Sobrenome das famílias: {sobrenome} ")

        case 3:
            break
        case _:
            print("Aba invalida ou inexistente. \nTente novamente.")
