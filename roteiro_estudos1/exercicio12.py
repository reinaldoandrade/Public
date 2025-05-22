# ------------------------------------------------------------------------------------------------------------
#   12- Desenvolver um cadastro de alunos, que deve solicitar o nome, curso, .
 
#   a. Você vai precisar adaptar uma lista e um dicionário para desenvolver essa atividade; 
#   b. Pode ser necessário adequar um dos loops de repetição para conseguir alcançar o 
#   resultado esperado. 
# ------------------------------------------------------------------------------------------------------------
nome =[]                            # Declara lista
curso =[]
while True:
    print("\n=== Cadastro de Aluno ===")
    nome_ = input("Nome (ou 'sair' para encerrar): ")
    if nome_.lower() == "sair":     # Retorna um string com todas as letras minúsculas e não afeta os demais caracteres.
        break
    curso_ = input("Curso: ")
    nome.append(nome_)              # Acrescenta um objeto ao final da lista
    curso.append(curso_) 

print("\n=== Alunos Cadastrados ===")
for i in range(len(nome)):
    print(f"Nome: {nome[i]}")
    print(f"Curso: {curso[i]}")
    print("\n", end='')             # Faz com que seja dada apenas uma única quebra de linha
    

