import os
from dataclasses import dataclass

os.system("cls || clear")


lista_familia = []

#Perguntas
@dataclass
class Familia:
    sobrenome: str
    numero_fiilhos: int

#Solicitando dados
familia = Familia(
    sobrenome = input("Digite o sobrenome da família: "),
    numero_fiilhos = int(input("Digite quantos filhos você tem: ")),
)
lista_familia.append(familia)

#Definido banco de dados
nome_do_arquivo = "pesquisa_prefeitura.txt"

#Abrindo arquivo e certificando a escrita de dados
with open(nome_do_arquivo, "a") as arquivo_familias:
    for familia in lista_familia:
        arquivo_familias