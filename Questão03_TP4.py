#Questão 03 do TP4

#Desenvolva um código que leia um arquivo contendo o nome e saldo da conta bancária
# de 15 clientes diferentes e ao final imprima na tela o nome
# e saldo da conta bancária de todos os clientes que têm saldo negativo na conta
# incluindo a seguinte mensagem: O cliente tem saldo negativo - entrar em contato,
# e além disso grave um arquivo contendo o nome e saldo da conta bancária
# de todos esses clientes que têm saldo negativo na conta.
# Para que o código possa ser elaborado corretamente, crie um arquivo
# contendo o nome e saldo da conta bancária de 15 clientes e defina alguns saldos negativos.

def lin():
    print("--" * 30)

def listar_contatos(arquivo_agenda):
    agenda = open(arquivo_agenda, 'r')
    contatos = agenda.read()
    contatos = contatos.splitlines()
    agenda.close()
    print(f"{'Contato':<30}\t{'Saldo - R$':>20}\t")
    for contato in contatos:
        contato = contato.split(',')
        nome = contato[0]
        saldo = contato[1]
        print(f"{nome:<30}\t{saldo:>20}\t")



def cadastrar_contato(nome, saldo, arquivo_agenda):
    agenda = open(arquivo_agenda, "a")
    if saldo < 0:
        agenda.write(f"{nome},{saldo}\r")
        agenda.close()


def boas_vindas():
  print("Agenda de clientes. Seja bem-vindo!")



lin()

boas_vindas()

lin()

arquivo_agenda = input("Informe o nome do arquivo de clientes a ser criado: ")

lin()

for c in range(0, 2):
    nome = input(f"Nome do cliente: ").upper().strip()
    saldo = float(input("Saldo do cliente: R$ "))
    cadastrar_contato(nome, saldo, arquivo_agenda)
    lin()
    print(f"\nCliente {nome} cadastrado com sucesso.")
    lin()


print("**********************************\n")
print("O(s) cliente(s) abaixo estão com saldo negativo - entrar em contato:")
listar_contatos(arquivo_agenda)
print("**********************************\n")





