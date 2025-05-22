# ------------------------------------------------------------------------------------------------------------
#   3- Utilizando a estrutura de repetição de sua escolha, escreva o código para imprimir na tela todas as 
#   possíveis horas e minutos do dia. Você não precisa se preocupar com muitos detalhes de formatação. 

#   Ou seja, o programa deve imprimir: 
#   0 : 0 
#   0 : 1 
#   0 : 2 
#   . 
#   . 
#   . 
#   23 : 58 
#   23 : 59 
# ------------------------------------------------------------------------------------------------------------

for hora in range(0,24):
    for min in range(0,60):
        print(f"{hora}:{min}")