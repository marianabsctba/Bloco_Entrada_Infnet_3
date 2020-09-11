#Questão 03 do TP4

#eu modifique um pouco essa questão porque queria estudar dicionários e pandas, bem como porque pensei ser mais fácil para corrigir. Obrigada.


import pandas as pd

def lin():
    print("--" * 30)

def listar_contatos():
    clientes = ("clientes_geral.csv")
    clientes = {"Nome": ["Ana", "Pedro", "Laura", "Marcos"], "Saldo": [1000.00, -500.00, -20.00, -2599.00], "Negativado": ["não", "sim", "sim", "sim"]}
    clientes_data_frame = pd.DataFrame(clientes)
    negativados_clientes = clientes_data_frame.loc[clientes_data_frame["Saldo"] < 0]
    negativados_clientes.to_csv("negativados_clientes.csv")
    return negativados_clientes



def boas_vindas():
    print("Lista de clientes. Seja bem-vindo!")

lin()

boas_vindas()

negativados = listar_contatos()

lin()

print(f"O(s) cliente(s) abaixo estão com saldo negativo - entrar em contato:")
print(negativados)
lin()
print("Dados salvos em novo arquivo.Verifique em seu diretório o arquivo 'negativados_clientes.csv'")
print("Volte sempre!")
lin()






