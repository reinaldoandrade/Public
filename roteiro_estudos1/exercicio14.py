# ------------------------------------------------------------------------------------------------------------
#   14- Escrever um programa para verificar se um número é primo. 
#   a. Números menores ou iguais a 1 não são primos 
#   b. 2 é o único número primo par 
#   c. Números pares maiores que 2 não são primos
# ------------------------------------------------------------------------------------------------------------

n = int(input("Digite um número:"))
if n < 0:
    print("Valor inválido. Digite apenas números positivos")
if n == 0 or n == 1:
    print(f"{n} Não é primo")
else:
    if n == 2:
        print("2 é primo")
    elif n % 2 == 0:
        print(f"{n} não é primo, pois 2 é o único número par primo.")
    else:
        x = 3
        while x < n:     # Enquanto 3 for menor que o número digitado
            if n % x == 0:
                break
            x = x + 2    # Soma-se de 2 em 2
        if x == n:       
            print(f"{n} é primo")
        else:
            print(f"{n} não é primo, pois é divisível por {x}")