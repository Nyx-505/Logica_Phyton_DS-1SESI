#  AULA COMPLETA: NUMEROS EM PYTHON
"""
Vamos aprender:
1- Tipos numéricos
2- Conversão de tipos
3- Hierarquia numérica
4- Operações matemáticas
5- Coerção de tipos
6- Verificação de tipos
7- Entrada de dados
"""
# ===========================
## Passo 01- Tipos Numéricos
# ===========================
# int -> Números Inteiros
# float -> Números com casas decimais
# complex -> Números Complexos (usado em matemática/engenharia)

print("===== TIPOS NUMÉRICOS =====")

# Exemplo 01- Numero Inteiro

# Criamos uma variável chamada numero_inteiro
numero_inteiro = 10

# Mostramos o valor
print ("Valor:", numero_inteiro)

# Type() mostra qual é o tipo da variável
print("Tipo:", type (numero_inteiro))

print("---------------------------")

# Exemplo 02- Numero Decimal

# Float é um numero com ponto decimal
numero_decimal = 3.14

print("Valor:", numero_decimal)
print("Tipo:", type(numero_decimal))

print("---------------------------")

# Exemplo 03- Numeros Complexos
# Um número complexo possui duas partes:
# Parte real (Numero normal)
# Parte Imaginária (multiplicada por j)

# Estrutura Geral:
# numero = a = bj

# a = parte real
# b = parte imaginária
# j = unidade imaginária

numero_complexo = 2 + 3j

print("Valor:", numero_complexo)
print("Tipo:", (numero_complexo))

print("---------------------------")

# Exemplo 03- Acessando cada parte do número

# .real retorna a parte real
print("Parte Real:", numero_complexo.real)

# .imag retorna a parte imaginária
print("Parte Imaginaria:", numero_complexo.imag)

# apenas para separar visualemnte a saída no terminal
print("\n\n")

# ===========================
## Passo 02- Conversão Tipos
# ===========================

## Exemplo Clássico:
## Dados vindo do ususário são textos (string), muitas vezes é necessario converter eles.

print("====== Conversões ======")

#float -> int

valor = int (3.9)

print("int(3.9):", valor)
print("Tipo:", type(valor))

#string -> int
valor1 =  "10"
print(type(valor1))

valor2 = int("10")
print('int("10"):', valor2)
print("tipo:", type(valor2))

#int --> Float
valor3 = float(10)
print("float(10):", valor3)
print("Tipo:", type(valor3))