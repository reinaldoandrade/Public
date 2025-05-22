# ------------------------------------------------------------------------------------------------------------
#   7- Faça um programa de computador que pergunte o valor total da compra e a forma de pagamento. 
#   Se o pagamento for em dinheiro, ocorrerá um desconto de 5% no valor da compra. Se o pagamento 
#   for no cartão, não terá desconto e ainda será cobrado uma taxa de 5%. O programa deve exibir: o 
#   valor da compra, o valor do desconto/acréscimo e o valor a ser pago.
 
#   a. Aqui você deve utilizar, If, Elif e Else para descobrir em qual categoria  
# ------------------------------------------------------------------------------------------------------------
total = float(input("Digiter o valor total da compra: "))
pagamento = input("para pagamento em espécie digite (dinheiro), para cartão digite (cartao): ")
if(pagamento == 'dinheiro'):
    print(f"valor da compra: R${total}")
    print(f"desconto: R${total*0.05}")
    print(f"valor a ser pago: R${(total - (total*0.05))}")
if(pagamento == 'cartao'):
    print(f"valor da compra: R${total}")
    print(f"acréscimo: R${total*0.05}")
    print(f"valor a ser pago: R${(total + (total*0.05))}")