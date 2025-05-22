# ------------------------------------------------------------------------------------------------------------
#   4- Criar um programa que calcule a área de um círculo. 
#   a. Recomendado trabalhar com uma variável do tipo float, por que o valor pode ser em casa 
#   decimal; 
#   b. Para calcular a área de um círculo o cálculo: A = π * r*r; 
#   c. Pode adotar como valor para pi=3.14.
# ------------------------------------------------------------------------------------------------------------
pi = 3.14
area = 0.0
raio =  float(input("Digite o valor do raio: "))
print(f"Área = {pi* (raio)**2}")