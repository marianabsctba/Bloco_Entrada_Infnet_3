#Questão 02

#Desenvolva um código que receba uma letra como entrada e imprima na tela a
#frase: A letra é uma consoante, caso seja realmente uma consoante e A letra é uma vogal, caso contrário.
#Para isso desenvolva uma função que receba a letra como entrada e retorne 1,
#caso seja uma consoante e 0, caso contrário.

def lin():
    print("==" * 40 )


def boas_vindas():
    print("Olá, seja bem-vindo ao programa que informa se a letra digitada é vogal ou consoante!")

lin()

boas_vindas()

lin()

def letras():
    letra = str(input("Digite apenas 01 (uma) letra qualquer: ")).upper().strip()
    print(f"Você digitou a letra {letra}.")
    vogal = "AEIOU"
    if letra in vogal:
        return 0
    else:
        return 1


def validar(letra):
    vogal = 0
    consoante = 1
    if letra == vogal:
        print(f"A letra digitada é uma vogal.")
    elif letra == consoante:
        print(f"A letra digitada é uma consoante.")


letra = letras()
validar(letra)
lin()
print("FIM!")




