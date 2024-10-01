import os
from dataclasses import dataclass

os.system("cls || clear")


Lista_familia = []

#Perguntas
@dataclass
class Familia:
    nome: str
    idade: int
    salario: float
    numero_fiilhos: int

#Solicitando dados
familia = Familia(
    nome = input("Digite seu nome: "),
    idade = int(input("Digite sua idade: ")),
    numero_fiilhos = int(input("Digite quantos filhos você tem: ")),
    salario = float(input("Digite qual o seu salário: "))
)
Lista_familia.append(familia)