
"""
Python - Estruturas de Repetição (while, for e range)

As estruturas de repetição permitem executar um bloco de código
várias vezes, de acordo com uma condição ou uma sequência de valores.

- while : repete o código enquanto uma condição for verdadeira.
- for   : percorre os elementos de uma sequência ou iterável.
- range(): gera uma sequência de números inteiros.
- continue: interrompe a iteração atual e passa para a próxima.
- break : encerra a estrutura de repetição imediatamente.
- else  : pode executar um bloco ao término normal de um laço.

Observação:
O for é frequentemente usado quando queremos percorrer uma sequência.
O while é útil quando a repetição depende de uma condição.
"""

# ==========================================================
# Exemplo 1 - Estrutura de repetição while
# ==========================================================

# O while continua executando enquanto a senha estiver incorreta.
senha_salva = "12345"
senha_digitada = ""
repeticoes = 0

while senha_salva != senha_digitada:
    # Conta cada tentativa realizada pelo usuário.
    repeticoes += 1

    # Solicita a senha até que ela esteja correta.
    senha_digitada = input(f"Tentativa {repeticoes} - Digite sua senha: ")

print("Senha correta!")
print(f"Total de tentativas: {repeticoes}")

print()

# ==========================================================
# Exemplo 2 - Percorrendo uma string com for
# ==========================================================

texto = "Python"

# Para cada letra presente em texto, exibe a letra atual.
for letra in texto:
    print(letra)

print()

# ==========================================================
# Exemplo 3 - Utilizando range()
# ==========================================================

# range(stop): gera números de 0 até stop - 1.
numero = range(10)

for valor in numero:
    print(valor)

print()

# ==========================================================
# Exemplo 4 - Definindo início e fim com range()
# ==========================================================

# range(start, stop): começa em 10 e termina antes de 20.
numero2 = range(10, 20)

for valor2 in numero2:
    print(valor2)

print()

# ==========================================================
# Exemplo 5 - Definindo o intervalo entre os números
# ==========================================================

# range(start, stop, step): avança de 2 em 2.
numero3 = range(10, 20, 2)

for valor3 in numero3:
    print(valor3)

print()

# ==========================================================
# Exemplo 6 - Utilizando range() com passo negativo
# ==========================================================

# O passo negativo permite percorrer os números em ordem decrescente.
# O valor final (-20) não é incluído na sequência.
numero4 = range(0, -20, -2)

for valor4 in numero4:
    print(valor4)

print()

# ==========================================================
# Exemplo 7 - Utilizando continue
# ==========================================================

# O continue ignora o restante da iteração atual
# e passa para a próxima repetição do laço.
for i in range(10):
    if i == 2:
        print("O valor de i é 2. Pulando esta iteração...")
        continue

    # Esta linha não será executada quando i for igual a 2.
    print(i)

print()

# ==========================================================
# Exemplo 8 - Utilizando else com for
# ==========================================================

# O else é executado quando o laço termina normalmente,
# sem ser interrompido por um break.
for x in range(6):
    print(x)
else:
    print("O laço terminou normalmente.")

print()

# ==========================================================
# Exemplo 9 - Utilizando break com for e else
# ==========================================================

# O break encerra o laço quando x é igual a 3.
# Nesse caso, o else não será executado.
for x in range(6):
    if x == 3:
        break

    print(x)
else:
    print("O laço terminou normalmente.")
