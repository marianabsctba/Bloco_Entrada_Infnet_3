#Desenvolva um código que leia o valor de compra para o estabelecimento
# e o preço de venda de 10 produtos diferentes
# e ao final imprima quantos produtos se enquadram em cada categoria abaixo:
#Cat 1: lucro < 10%
#Cat 2: 10% <= lucro <= 20%
#Cat 3: lucro > 20%

def get_data():

    valor_compra = float(input(f"Digite o valor de compra do produto: R$ "))
    valor_venda = float(input(f"Digite o valor de venda do produto: R$ "))
    lucro = ((valor_venda - valor_compra) / valor_venda) * 100
    round(lucro)
    return lucro


list_1 = []
list_2 = []
list_3 = []

for p in range(0, 10):
    valor = get_data()
    if valor < 10:
        list_1.append(valor)
    elif 10 <= valor <= 20:
        list_2.append(valor)
    elif valor > 20:
        list_3.append(valor)

quantidade_valor_1 = len(list_1)
quantidade_valor_2 = len(list_2)
quantidade_valor_3 = len(list_3)

print(f"Na Cat 1 há {len(list_1)} produto(s).")
print(f"Na Cat 2 há {len(list_2)} produto(s).")
print(f"Na Cat 3 há {len(list_3)} produtos(s).")












