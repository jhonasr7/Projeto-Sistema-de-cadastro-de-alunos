alunos = []


def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = float(input("Digite a nota do aluno: "))

    while nota < 0 or nota > 10:
        print("Nota inválida. Digite uma nota entre 0 e 10.")
        nota = float(input("Digite a nota do aluno: "))

    aluno = {
        "nome": nome,
        "idade": idade,
        "nota": nota
    }

    alunos.append(aluno)


def listar_alunos():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Nota:", aluno["nota"])
            print()


def buscar_aluno():
    nome_busca = input("Digite o nome do aluno: ")
    encontrado = False

    for aluno in alunos:
        if aluno["nome"] == nome_busca:
            print("Nome:", aluno["nome"])
            print("Idade:", aluno["idade"])
            print("Nota:", aluno["nota"])
            encontrado = True

    if encontrado == False:
        print("Aluno não encontrado.")


def remover_aluno():
    nome_busca = input("Digite o nome do aluno: ")
    encontrado = False

    for aluno in alunos:
        if aluno["nome"] == nome_busca:
            alunos.remove(aluno)
            encontrado = True
            break

    if encontrado == False:
        print("Aluno não encontrado.")
    else:
        print("Aluno removido com sucesso.")


def mostrar_media():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        soma = 0

        for aluno in alunos:
            soma += aluno["nota"]

        media = soma / len(alunos)

        print("Média geral:", media)


while True:
    print("1 - Adicionar aluno")
    print("2 - Listar todos os alunos")
    print("3 - Buscar aluno pelo nome")
    print("4 - Remover aluno")
    print("5 - Mostrar média geral das notas")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_aluno()

    elif opcao == "2":
        listar_alunos()

    elif opcao == "3":
        buscar_aluno()

    elif opcao == "4":
        remover_aluno()

    elif opcao == "5":
        mostrar_media()

    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")