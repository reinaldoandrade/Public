# ------------------------------------------------------------------------------------------------------------
#   11- Escrever um programa que solicite um número de 1 a 9 e imprima a tabuada do número digitado. 

#   a. Aqui devemos trabalhar com um for e determinar que ele comece de 1 até 11.  
#   b. Deve ser utilizado If, Elif e Else para validar a entrada de dados do usuário.
# # ------------------------------------------------------------------------------------------------------------
numero = input("Digite um número de 1 a 9: ")
if numero.isdigit():
    numero = int(numero)
    if numero>=1 and numero<=9:
        for i in range(1,11):
            print(f"{numero} x {i}")

