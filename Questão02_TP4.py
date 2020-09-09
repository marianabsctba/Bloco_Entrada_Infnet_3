#Questão 02

#Desenvolva um código que receba uma letra como entrada e imprima na tela a
#frase: A letra é uma consoante, caso seja realmente uma consoante e A letra é uma vogal, caso contrário.
#Para isso desenvolva uma função que receba a letra como entrada e retorne 1,
#caso seja uma consoante e 0, caso contrário.

def letras():
    letra = str(input("Digite uma letra qualquer: ")).upper().strip()
    print(f"Você digitou a letra {letra}.")
    vogal = "AEIOU"
    if letra in vogal:
        return 0
    else:
        return 1


def validar():
    vogal = 0
    consoante = 1
    if letra == vogal:
        print(f"A letra digitada é uma vogal.")
    elif letra == consoante:
        print(f"A letra digitada é uma consoante.")

letra = letras()
validar()









