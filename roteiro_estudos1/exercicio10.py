# ------------------------------------------------------------------------------------------------------------
# 10- Faça um programa que receba 20 elementos reais digitados pelo usuário e calcule e retorne a soma 
# dos números múltiplos de 19 que foram digitados pelo usuário. 
 
# a. Aqui deve ser adotada uma estrutura de repetição para receber os valores. 
# b. Múltiplos de 19 são números que ao serem divididos por 19 deixam como resto da divisão 0.
# ------------------------------------------------------------------------------------------------------------
soma = 0
for i in range(1,21):
    numero = int(input(f"Digite o número {i}: "))
    if (numero% 19 == 0):
        soma += numero
print(f"Os números múltiplos de 19, somados resultam em: {soma}")