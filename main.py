from controle_gastos import ControleDeGastos,Gastos

despesas = ControleDeGastos()
while True:
    descricao = Gastos(
            input('\033[32mDigite o local do gasto: \033[m'),
            input('\033[32mDigite a data: \033[m'),
            input('\033[32mDigite o valor: \033[m'))

    despesas.inserir_gastos(descricao)

    pergunta = input('\033[36mQuer continuar\033[m[S/N]: ').upper()[0]
    if pergunta == 'N':
        break

despesas.lista_gastos()
print(
    f'\033[35mO total de gastos foi de:\033[m R$ \033[31m{despesas.soma_gastos():.2f}\033[m'
    )
