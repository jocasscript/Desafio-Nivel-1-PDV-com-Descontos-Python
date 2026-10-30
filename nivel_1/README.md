# Desafio Nível 1 — PDV com Descontos

## O que o código faz

O programa simula um PDV (Ponto de Venda) no terminal. Recebe o valor da compra e a idade do cliente, aplica descontos progressivos e mostra o valor final com duas casas decimais. Permite registrar várias compras e, ao encerrar, apresenta a quantidade de compras, o total bruto, o total de descontos e o total final.

## Como ele faz

1. Cria a lista `compras` para guardar os registros.
2. Solicita o valor da compra, aceitando ponto ou vírgula como separador decimal. Não use separador de milhar.
3. Verifica o texto digitado antes de convertê-lo para número. Entradas inválidas e números negativos geram um aviso e são solicitados novamente.
4. Se o valor informado for zero, encerra o cadastro sem solicitar a idade nem registrar uma compra.
5. Solicita a idade, que deve ser um número inteiro não negativo.
6. Aplica 20% de desconto quando a idade é maior ou igual a 65 anos.
7. Verifica se o valor após esse desconto é estritamente maior que R$ 100,00. Se for, aplica mais 10% sobre esse valor.
8. Arredonda o valor final para duas casas decimais e calcula o desconto concedido.
9. Adiciona à lista um dicionário com o valor original, a idade, o desconto e o valor final, usando `.append()`.
10. Exibe o resultado e volta a solicitar a próxima compra.
11. Ao encerrar, percorre a lista com `for`, soma os valores e apresenta o resumo do dia.

Uma compra de R$ 200,00 para uma pessoa de 65 anos passa para R$ 160,00 após o desconto por idade e depois para R$ 144,00 com o desconto por valor. O desconto acumulado é de 28%.

## Organização e ferramentas

O código segue uma estrutura procedural e sequencial em um único arquivo, com condicionais `if`, laços `while` e `for`, lista e dicionários. Conforme a orientação da atividade, não utiliza `def` nem `try/except`. A validação é feita por condições e métodos de texto antes das conversões numéricas.

Foram utilizados Python 3, o terminal e a biblioteca padrão `math`, cuja função `isfinite()` verifica se o valor numérico é finito. Não é necessário instalar pacotes adicionais. O histórico permanece em memória durante a execução.

## Como rodar

Abra o terminal dentro da pasta `nivel_1` e execute:

```bash
python pdv.py
```

Se o seu sistema usa `python3`, execute `python3 pdv.py`.

## Tabela de exemplos

O desconto por valor é aplicado depois do desconto por idade.

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

Digite os valores e as idades da tabela e, depois da última compra, informe zero. O resumo esperado é:

- Quantidade de compras registradas: **10**.
- Total bruto: **R$ 2156.00**.
- Total de descontos concedidos: **R$ 447.10**.
- Total final: **R$ 1708.90**.

### Casos-limite

- **R$ 125,00 e idade 70:** após 20%, o valor fica em R$ 100,00 e não recebe o desconto extra.
- **R$ 200,00 e idade 64:** recebe apenas 10% de desconto, resultando em R$ 180,00.
- **R$ 101,00 e idade 30:** o resultado é R$ 90,90.
- **Zero na primeira entrada:** o resumo apresenta quantidade e totais zerados.
- **Entradas negativas ou inválidas:** o programa avisa e solicita novamente o dado.