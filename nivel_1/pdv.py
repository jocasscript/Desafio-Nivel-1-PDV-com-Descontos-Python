"""Desafio Nível 1: PDV com descontos progressivos."""

from math import isfinite


def calcular_valor_final(valor, idade):
    """Aplica primeiro o desconto por idade e depois o desconto por valor."""
    valor_final = valor

    if idade >= 65:
        valor_final *= 0.80

    # Esta comparação usa o valor depois do desconto por idade.
    if valor_final > 100:
        valor_final *= 0.90

    return round(valor_final, 2)


def main():
    compras = []

    print("=== PDV COM DESCONTOS ===")
    print("Digite 0 no valor da compra para encerrar.")

    while True:
        try:
            entrada = input("\nValor da compra (R$): ").strip().replace(",", ".")
            valor = float(entrada)
        except ValueError:
            print("Valor inválido. Digite um número, como 125.00 ou 125,00.")
            continue

        if not isfinite(valor):
            print("Valor inválido. Digite um número finito.")
            continue

        if valor < 0:
            print("O valor não pode ser negativo. Digite novamente.")
            continue

        if valor == 0:
            break

        while True:
            try:
                idade = int(input("Idade do cliente: "))
            except ValueError:
                print("Idade inválida. Digite um número inteiro.")
                continue

            if idade < 0:
                print("A idade não pode ser negativa. Digite novamente.")
                continue

            break

        valor_final = calcular_valor_final(valor, idade)
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


if __name__ == "__main__":
    main()

