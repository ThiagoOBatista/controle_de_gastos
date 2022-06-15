class ControleDeGastos:
    def __init__(self):
        self.despesas = []

    def inserir_gastos(self, despesa):
        self.despesas.append(despesa)

    def lista_gastos(self):
        for despesa in self.despesas:
            print(f'\033[34mO local da compra:\033[m {despesa.local}')
            print(f'\033[34mA data da compra:\033[m {despesa.data}')
            print(f'\033[34mO valor:\033[m {despesa.valor}')

    def soma_gastos(self):
        total = 0
        for gastos in self.despesas:
            total += gastos.valor
        return total

class Gastos:
    def __init__(self, local, data, valor):
        self.local = local
        self.data = int(data)
        self.valor = float(valor)