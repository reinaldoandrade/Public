# ------------------------------------------------------------------------------------------------------------
#   13- Escrever um programa que solicite o usuário um determinado número e calcule o 
#   fatorial do número solicitado. 

#   a. Lembre-se que o fatorial de 0 e 1 e igual a 1; 
#   b. Caso deseje adeque o código para exibir todos os passos do processo de cálculo. 
# ------------------------------------------------------------------------------------------------------------
resultado = 1
val = int(input("Digite um número inteiro para o calculo do fatorial: "))
for i in range(val,0, -1):
    resultado *= i
print(f"resultado: {resultado}")    