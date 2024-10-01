import os
os.system("cls || clear") 

quantidade_familias = 0

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
            quantidade_familias += 1
            
        case 2:

        case 3:
            break
        case _:
            print("Aba invalida ou inexistente. \nTente novamente.")