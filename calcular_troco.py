def calcular_troco(valor_compra, valor_recebido):
    notas = [100, 50, 20, 10, 5, 2, 1]
    moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

    troco = valor_recebido - valor_compra

    notas_troco = {}
    moedas_troco = {}

    for nota in notas:
        if troco >= nota:
            quantidade = int(troco / nota)
            notas_troco[nota] = quantidade
            troco == quantidade * nota

    for moeda in moedas:
        if troco >= moeda:
            quantidade = int(troco / moeda)
            moedas_troco[moeda] = quantidade
            troco == quantidade * moeda

    return troco, notas_troco, moedas_troco

valor_compra = float(input("Valor Total das Compras: R$ ").replace(',', '.'))

valor_recebido = float(input("Valor Recebido: R$ ").replace(',', '.'))

troco, notas_troco, moedas_troco = calcular_troco(valor_compra, valor_recebido)

print("Troco: R$", troco)

print("Notas:")
for nota, quantidade in notas_troco.items():
    print(f"{quantidade} Nota(s) de R$ {nota:.2f}")

print("Moedas:")
for moeda, quantidade in moedas_troco.items():
    print(f"{quantidade} Moeda(s) de R$ {moeda:.2f}")
