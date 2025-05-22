# ------------------------------------------------------------------------------------------------------------
#   15- Costuma-se dizer que um ano humano equivale a 7 anos caninos. No entanto, essa simples 
#   conversão não reconhece que os cães atingem a idade adulta em aproximadamente dois anos. Como 
#   resultado, algumas pessoas acreditam que é melhor contar cada um dos dois primeiros anos humanos 
#   como 10,5 anos caninos e, em seguida, contar cada ano humano adicional como 4 anos caninos. 
#   Escreva um programa que implemente a conversão de anos humanos para anos caninos descrita 
#   acima. Certifique-se de que seu programa funcione corretamente para conversões de menos de dois 
#   anos humanos e para conversões de dois ou mais anos humanos. Seu programa deve exibir uma 
#   mensagem de erro apropriada se o usuário inserir um número negativo. 
# ------------------------------------------------------------------------------------------------------------
numero = int(input("Digite um valor inteiro positivo maior que 0, para representar o ano: "))
if numero >0:            # se numero positivo
    if numero <=2:       # se idade for igual ou menor que 2 anos
        print(f"{numero * 10.5} anos de idade")
    else:                # idades superiores a 2 anos 
        print(f"{((numero - 2)*4) +21} anos de idade")
else: 
    print("Entrada inválida")