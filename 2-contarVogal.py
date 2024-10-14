##############################################################################################################################
# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula,
# além de informar a quantidade de vezes em que ela ocorre.
##############################################################################################################################
nome = str(input("digite uma palavra: ")) # recebe o nome para fazer a buscar pela vovla 'a'
total = (nome.lower()).count("a")         # converte o texte para letras minisculas e conta as incidências da vogal 'a'
texto = "vogal" if total == 1 else "vogais"

if total > 0:
    print(f"A palavra {nome} tem {total} {texto} 'a'.")
    
else:
    print(f"A palavra {nome} não possui nenhuma vogal 'a'.")
