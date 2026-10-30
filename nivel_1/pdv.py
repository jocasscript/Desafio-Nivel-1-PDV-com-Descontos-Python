"""Desafio Nível 1: PDV com descontos progressivos."""

from math import isfinite

compras = []

print("=== PDV COM DESCONTOS ===")
print("Digite 0 no valor da compra para encerrar.")

while True:
    entrada_valor = input("\nValor da compra (R$): ").strip().replace(",", ".")

    # Confere o texto antes da conversão para número.
    texto_valor = entrada_valor
    if texto_valor.startswith("-"):
        texto_valor = texto_valor[1:]

    if not texto_valor.isascii() or not texto_valor.replace(".", "", 1).isdigit():
        print("Valor inválido. Digite um número, como 125.00 ou 125,00.")
        continue

    valor = float(entrada_valor)

    if not isfinite(valor):
        print("Valor inválido. Digite um número finito.")
        continue

    if valor < 0:
        print("O valor não pode ser negativo. Digite novamente.")
        continue

    if valor == 0:
        break

    while True:
        entrada_idade = input("Idade do cliente: ").strip()

        texto_idade = entrada_idade
        if texto_idade.startswith("-"):
            texto_idade = texto_idade[1:]

        if not texto_idade.isascii() or not texto_idade.isdigit():
            print("Idade inválida. Digite um número inteiro.")
            continue

        idade = int(entrada_idade)

        if idade < 0:
            print("A idade não pode ser negativa. Digite novamente.")
            continue

        break

    valor_final = valor

    if idade >= 65:
        valor_final *= 0.80

    # O desconto extra considera o valor após o desconto por idade.
    if valor_final > 100:
        valor_final *= 0.90

    valor_final = round(valor_final, 2)
    desconto = round(valor - valor_final, 2)

    compras.append({
        "valor_original": valor,
        "idade": idade,
        "desconto": desconto,
        "valor_final": valor_final,
    })

    print(f"Valor original: R$ {valor:.2f}")
    print(f"Desconto concedido: R$ {desconto:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}")

total_bruto = 0.0
total_descontos = 0.0
total_final = 0.0

for compra in compras:
    total_bruto += compra["valor_original"]
    total_descontos += compra["desconto"]
    total_final += compra["valor_final"]

print("\n=== RESUMO DO DIA ===")
print(f"Quantidade de compras registradas: {len(compras)}")
print(f"Total bruto: R$ {total_bruto:.2f}")
print(f"Total de descontos concedidos: R$ {total_descontos:.2f}")
print(f"Total final: R$ {total_final:.2f}")
