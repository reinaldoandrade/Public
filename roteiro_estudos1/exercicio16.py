# ------------------------------------------------------------------------------------------------------------
#   16- Desenvolver uma calculadora simples, a mesma deve realizar +, -, *, /, ela deve ficar 
#   em loop e deve ser utilizado sair para terminar o loop. 

#   a. Apresente em um menu as opções para o usuário; 
#   2 de 3 
#   b. Antes de fazer a divisão, verifique se o segundo valor e =0; 
#   c. Selecione uma estrutura de repetição para manter o Loop ativo; 
#   d. Valide as opções na entrada de dados, caso o usuário digite uma operação invalida  
#   e. Utilize If, Elif e Else para validar as opções de entrada do usuário.  
# ------------------------------------------------------------------------------------------------------------

while True:         # loop para o código todo

    while True:     # leitura e validação do primeiro número
        entrada1 = input("Digite o 1° número ou 'sair' para finalizar: ")
        if entrada1.isdigit():            # Se for um valor númerico 
            entrada1 = float(entrada1)
            break                         # encerra a leitura
        elif entrada1 == 'sair':
            exit()                        # encerra a execução do código, torna desnecessário um break para encerrar a leitura  e de outro break externo a este while de leitura para encerrar o código              
            # break
        else:  
            print("\nEntrada inválida, digite novamente\n")

    # if entrada1 == 'sair':              # Esse if encerraria o código caso tivesse usado comando break no lugar do exit() no trecho acima  
        # break
    while True:
        entrada2 = input("Digite o 2° número ou 'sair' para finalizar: ")
        if entrada2.isdigit():
            entrada2 = float(entrada2)
            break
        elif entrada2 == 'sair':
            exit()
        else: 
            print("\nEntrada inválida, digite novamente\n")
   
    print("\n1- adição\n2- subtração\n3- multiplicação\n4- divisão:\n ")

    while True:
        operacao = input("Digite a operação ou 'sair' para finalizar: ")
        if operacao.isdigit():
            break
        elif operacao == 'sair':
            exit()
        else: 
            print("\nEntrada inválida, digite novamente\n")

    

    if operacao == '1':
        print(f"\nRESULTADO: {entrada1 + entrada2}")        # 1- adição  
    elif operacao == '2':
        print(f"\nRESULTADO: {entrada1 - entrada2}")        # 2- subtração
    elif operacao == '3':
        print(f"\nRESULTADO: {entrada1 * entrada2}")        # 3- multiplicação
    elif operacao == '4': 
        if entrada2 != 0:                                        # Se o denominador da divisão for DIFERENTE de zero
            print(f"\nRESULTADO: {entrada1 / entrada2}")    # 4- divisão
        else:                                                    # Se denominador igual a zero
            print("\nEntrada inválida, a operação não pode ser realizada")
    else:
        print("\nEntrada inválida")

