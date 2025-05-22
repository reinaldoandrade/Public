# ------------------------------------------------------------------------------------------------------------
#   6- Criar um programa que verifique se um número é par ou ímpar.
 
#   a. Todo número par deixa como resto divisão 0, então se você comprar se o resto da divisão do 
#   número digitado pelo usuário e igual a 0 o número é par.
# ------------------------------------------------------------------------------------------------------------

numero = int(input("Digite um número: "))
if(numero%2 == 0):
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")
