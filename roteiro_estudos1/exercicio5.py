# ------------------------------------------------------------------------------------------------------------
#   5- Escrever um programa que converta temperatura de Celsius para Fahrenheit. 
#   a. Recomendado trabalhar com uma variável do tipo float; 
#   b. Converter para Fahrenheit (F = (C * 9/5) + 32) 
# ------------------------------------------------------------------------------------------------------------
celcius = float(input("Digite a temperatura: "))
print(f"Temperatura = {(celcius* (9/5)+32):.2f}")