"""1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?"""

indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

print(soma)

"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""

numero = int(input("Informe um número: "))

a, b = 0, 1
fibonacci = False

while b <= numero:
    if b == numero or numero == 0:
        fibonacci = True
        break
    a, b = b, a + b

if fibonacci:
    print(f"O número {numero} pertence a sequência de Fibonacci")
else:
    print(f"O número {numero} não pertence a sequência de Fibonacci")

"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal."""

faturamento_di = [1300, 5000, 1900, 4500, 2000, 750, 0, 3000, 3000, 1500, 1000, 1300, 1300, 3400, 650, 4500, 500, 750, 500, 3000, 3000, 1500, 1000, 1300, 0, 0, 500, 800, 3000, 1500]

faturamento_di_sem_zero = []

for n in faturamento_di:
    if n > 0:
        faturamento_di_sem_zero.append(n)

faturamento_minimo = min(faturamento_di_sem_zero)
faturamento_maximo = max(faturamento_di_sem_zero)
faturamento_medio = sum(faturamento_di_sem_zero)/len(faturamento_di_sem_zero)

faturamento_acima_media = []
contagem_dias = 0
for n in faturamento_di_sem_zero:
    if n > faturamento_medio:
        faturamento_acima_media.append(n)
        contagem_dias += 1

print(f"O faturamento mínimo ocorrido em um mês foi de R$ {faturamento_minimo}")
print(f"O faturamento máximo ocorrido em um mês foi de R$ {faturamento_maximo}")
print(f"O faturamento médio mensal foi de R$ {faturamento_medio:.2f}")
print(f"Os valores de faturamento que superaram a média mensal foram: {faturamento_acima_media} em reais.")
print(f"A quantidade de dias que o faturamento superou a média mensal foram de: {contagem_dias} dias.")

"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP - R$67.836,43
• RJ - R$36.678,66
• MG - R$29.229,88
• ES - R$27.165,48
• Outros - R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora."""

valor_estados = {"SP": 67836.43, "RJ": 36678.66, "MG": 29229.88, "ES": 27165.48, "Outros": 19849.53}
faturamento_total = sum(valor_estados.values())

for estado, valor in valor_estados.items():
    valor_percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {valor_percentual:.2f}%")


"""5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;"""

string = input("Digite uma palavra para inverter: ")
string_invertida = ""

for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

print("String invertida:", string_invertida)