"""
Python - Estruturas Condicionais (if, elif e else)

As estruturas condicionais permitem que o programa tome decisões
com base em uma condição.

- if   : executa um bloco de código se a condição for verdadeira.
- elif : verifica uma nova condição caso a anterior seja falsa.
- else : executa um bloco de código quando nenhuma das condições
         anteriores é satisfeita.
"""

# ==========================================================
# Exemplo 1 - Verificando a opção informada pelo usuário
# ==========================================================

# Solicita que o usuário escolha uma das opções.
login = input('Digite "Entrar" ou "Sair": ')

# Verifica a opção informada pelo usuário.
if login == "Entrar":
    print("Você entrou no sistema.")

# Executado apenas se a condição anterior for falsa.
elif login == "Sair":
    print("Você saiu do sistema.")

# Executado quando nenhuma das condições anteriores é verdadeira.
else:
    print('Você não digitou "Entrar" nem "Sair".')

print()

# ==========================================================
# Exemplo 2 - Fluxo de execução do if / elif / else
# ==========================================================

# O Python verifica as condições de cima para baixo.
# Assim que encontra a primeira condição verdadeira,
# executa aquele bloco e ignora os demais.

# Importante:
# Apenas o primeiro bloco cuja condição for verdadeira será executado.
# As demais condições não serão verificadas.

condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print("Código para a condição 1")
elif condicao2:
    print("Código para a condição 2")
elif condicao3:
    print("Código para a condição 3")
elif condicao4:
    print("Código para a condição 4")
else:
    print("Nenhuma condição foi satisfeita.")