# Desafio Nível 1 — PDV com Descontos

## O que o código faz

O programa simula um PDV (Ponto de Venda) no terminal. Ele recebe o valor de cada compra e a idade do cliente, aplica os descontos previstos no desafio e mostra o valor final com duas casas decimais. Cada compra é guardada em uma lista. Ao encerrar, o programa apresenta a quantidade de compras, o total bruto, o total de descontos concedidos e o total final.

## Como ele faz

1. Cria a lista `compras` para armazenar os registros.
2. Pede o valor da compra. Aceita ponto ou vírgula como separador decimal, por exemplo `125.00` ou `125,00`. Não use separador de milhar.
3. Se o valor for negativo ou inválido, mostra uma mensagem e pede novamente.
4. Se o valor for `0`, encerra o cadastro e mostra o resumo. Nesse caso, não pede a idade e não registra uma compra.
5. Para uma compra com valor positivo, pede a idade. Se ela for negativa ou não for um número inteiro, pede novamente.
6. Aplica 20% de desconto se a idade for maior ou igual a 65 anos.
7. Verifica o valor resultante do passo anterior. Se ele for estritamente maior que R$ 100, aplica mais 10% sobre esse valor.
8. Arredonda o valor final para duas casas decimais, calcula o desconto concedido e guarda a compra na lista usando `.append()`.
9. Mostra o resultado da compra e volta a pedir o valor da próxima compra.
10. Ao encerrar, percorre os registros com `for` e soma os valores para exibir o resumo do dia.

Os descontos são progressivos: uma compra de R$ 200,00 para uma pessoa de 65 anos passa para R$ 160,00 com o primeiro desconto e depois para R$ 144,00 com o segundo. O desconto total é de 28%.

## Como rodar

É necessário ter Python 3 instalado. O programa usa somente a biblioteca padrão e não precisa de instalação de pacotes.

Abra o terminal dentro da pasta `nivel_1` e execute:

```bash
python pdv.py
```

Se o seu sistema usa o comando `python3`, execute `python3 pdv.py`.

## Tabela de exemplos

A coluna “Desconto valor” indica o percentual aplicado depois do desconto por idade.

|  # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|----|------------|-------|----------------|----------------|----------------------|
|  1 |      50.00 |    30 |             0% |             0% |             R$ 50.00 |
|  2 |     100.00 |    30 |             0% |             0% |            R$ 100.00 |
|  3 |      80.00 |    65 |            20% |             0% |             R$ 64.00 |
|  4 |     100.00 |    70 |            20% |             0% |             R$ 80.00 |
|  5 |     125.00 |    70 |            20% |             0% |            R$ 100.00 |
|  6 |     200.00 |    30 |             0% |            10% |            R$ 180.00 |
|  7 |     101.00 |    30 |             0% |            10% |             R$ 90.90 |
|  8 |     200.00 |    65 |            20% |            10% |            R$ 144.00 |
|  9 |    1000.00 |    80 |            20% |            10% |            R$ 720.00 |
| 10 |     200.00 |    64 |             0% |            10% |            R$ 180.00 |

Para conferir, execute o programa e digite o valor e a idade de cada linha. Após a última compra, digite `0`. Para essas dez compras, o resumo esperado é:

- Quantidade de compras registradas: **10**.
- Total bruto: **R$ 2156.00**.
- Total de descontos concedidos: **R$ 447.10**.
- Total final: **R$ 1708.90**.

### Casos-limite

- **R$ 125,00 e idade 70:** após 20%, o valor fica em R$ 100,00. Como ele não é maior que 100, não há desconto extra.
- **R$ 200,00 e idade 64:** não há desconto por idade. Aplica-se apenas 10%, resultando em R$ 180,00.
- **R$ 101,00 e idade 30:** o desconto de 10% resulta em R$ 90,90.
- **Encerrar imediatamente:** digitar `0` antes de registrar compras mostra quantidade zero e todos os totais zerados.
- **Entradas negativas:** o programa avisa e pede novamente, sem registrar a entrada inválida.

## Arquivos da entrega

- `pdv.py`: código do programa.
- `README.md`: documentação, instruções e tabela de exemplos.

Esta entrega implementa os requisitos obrigatórios do desafio. Os bônus de quantidade, cupom e arquivo de histórico são opcionais e não estão ativados.

