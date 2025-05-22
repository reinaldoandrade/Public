# ------------------------------------------------------------------------------------------------------------
#   8- Faça um programa de computador que imprima todos os divisores positivos de um número digitado 
#   pelo usuário. Exemplo: se o usuário digitar 10, os divisores serão: 1, 2, 5 e 10. Ou seja, números 
#   que não sobrariam restos em uma possível divisão.
# ------------------------------------------------------------------------------------------------------------

numero = int(input("Digite um número inteiro: "))
if numero < 0:
    numero = numero * -1
for i in range (1,numero): 
    if numero % i == 0:
        print(i)
