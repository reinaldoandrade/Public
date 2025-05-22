# ------------------------------------------------------------------------------------------------------------
#   1- Faça um programa que receba 20 elementos reais digitados pelo usuário e calcule e retorne a soma 
#   dos números ímpares e números pares.
  
#   a. Aqui deve ser adotada uma estrutura de repetição para receber os valores. 
#   b. Em caso dos números pares e impares deve-se selecionar qual condição se deseja verificar 
#   primeiro se o numero e par ou impar.    
# ------------------------------------------------------------------------------------------------------------

entrada = 0
impar = 0
par = 0
for i in range(0,20):
    entrada = int(input(f"Digite o número {i}: "))
    if(entrada %2 ==0):
        par+= entrada
    else:
        impar+= entrada
print(f"soma dos numero pares: {par} ímpares: {impar}")