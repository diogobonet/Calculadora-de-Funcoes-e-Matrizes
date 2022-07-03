import json

filePrincipal = 'Matriz.json'
fileMult = 'MultMatriz.json'

#Matriz principal que será salva.
matrizPrincipal = []
matrizMult = []


#Def ler json.
def loadDb(variavel, file):
    with open(file, 'r') as rMatriz:
        variavel = json.load(rMatriz)
    return variavel


#Leitura da matriz salva.
matrizPrincipal = loadDb(matrizPrincipal, filePrincipal)
matrizMult = loadDb(matrizMult, fileMult)


#Def salvar em json.
def saveDb(data, file):
    with open(file, 'w') as wMatriz:
        json.dump(data, wMatriz)


#Def topo do menu principal. (Estética)
def menuMatrizTopo():
    print("="*55)
    print("                    MenuMatrizes")
    print("="*55)


#Def menu de escolhas do menu de matrizes.
def menuMatrizPrincipal():
    while True:
        print("\n\033[0;33m[ 1 ] | Criar Matriz")
        print("[ 2 ] | Determinante 2x2")
        print("[ 3 ] | Determinante 3x3")
        print("[ 4 ] | Transposta")
        print("[ 5 ] | Criar Matriz para Multiplicar")
        print("[ 6 ] | Multiplicação")
        print("\033[31m[ 7 ] | Sair")
        op = input("\033[0;0m-> ")
       
        if op == "1":
            criarMatriz()

        elif op == "2":
            det2x2()

        elif op == "3":
            det3x3()

        elif op == "4":
            matrizTransposta()

        elif op == "5":
            criarMatrizMult()

        elif op == "6":
            multiplicacaoM()

        elif op == "7":
            print("\033[0;91mSaindo...\033[0;0m")
            break

        else:
            menuMatrizPrincipal()
    from main import menuPrincipal
    menuPrincipal()


#Def de mostrar matriz como matriz, e não lista.
def mostrarMatriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])
    print('\n')


#Def de criar a matriz de qualquer tamanho.
def criarMatriz():
    if matrizPrincipal != []:
        opdel = input('Deseja continuar? a matriz existente será deletada!\n(S) para continuar: ')
        if opdel == 'S' or opdel == 's':
            matrizPrincipal.clear()
            print('\n \033[0;32mMatriz Excluida com sucesso!\u001b[0m \n')
            saveDb(matrizPrincipal, filePrincipal)
        else:
            menuMatrizPrincipal()
    matriz_linhas = int(input('Quantidade de linhas: '))
    matriz_colunas = int(input('Quantidade de colunas: '))
    matcontrol = 0


    for quantLinhas in range(0, matriz_linhas):
        matrizPrincipal.append(0)
        matrizMenor = []
        for c in range(0, matriz_colunas):
            matrizMenor.append(0)
        matrizPrincipal[matcontrol] = matrizMenor
        matcontrol += 1


    mostrarMatriz(matrizPrincipal)


    for linha in range(0, matriz_linhas):
        for coluna in range(0, matriz_colunas):
            print(f'Linha[{linha}] Coluna[{coluna}]:')
            matrizPrincipal[linha][coluna] = float(input(f'Digite valor para {linha, coluna}: '))
            mostrarMatriz(matrizPrincipal)
    saveDb(matrizPrincipal, filePrincipal)
    from main import menuPrincipal
    menuPrincipal()


#Def de determinante de uma matriz 2x2.
def det2x2():
#Verificador se é uma matriz 2x2.
    verify2L = 0
    verify2C = 0
    for l in range(0, len(matrizPrincipal)):
        verify2L += 1
        for c in matrizPrincipal[l]:
            verify2C += 1
    if verify2L == 2 and verify2C == 4:
#Achando o determinante da Matriz caso ela seja 2x2.
        determinante2x2 = (matrizPrincipal[0][0] * matrizPrincipal[1][1]) - (matrizPrincipal[0][1] * matrizPrincipal[1][0])
        print(f'\033[0;32mdet(2x2) = {determinante2x2}\u001b[0m')
        input('[ENTER] para continuar...')
        print('\n')
        from main import menuPrincipal
        menuPrincipal()
    else:
        print('Não é possível fazer determinante com essa matriz!')


def det3x3():
#Verificador se é uma matriz 3x3.
    verify3L = 0
    verify3C = 0
    for l in range(0, len(matrizPrincipal)):
        verify3L += 1
        for c in matrizPrincipal[l]:
            verify3C += 1
    if verify3L == 3 and verify3C == 9:
        determinante3x3L1 = (matrizPrincipal[0][0] * matrizPrincipal[1][1] * matrizPrincipal[2][2])+(matrizPrincipal[0][1] * matrizPrincipal[1][2] * matrizPrincipal[2][0])+(matrizPrincipal[0][2] * matrizPrincipal[1][0] * matrizPrincipal[2][1])
        determinante3x3L2 = (matrizPrincipal[0][2] * matrizPrincipal[1][1] * matrizPrincipal[2][0])+(matrizPrincipal[0][0] * matrizPrincipal[1][2] * matrizPrincipal[2][1])+(matrizPrincipal[0][1] * matrizPrincipal[1][0] * matrizPrincipal[2][2])
        determinante3x3 = (determinante3x3L1 - determinante3x3L2)
        print(f'\033[0;32mdet(3x3) = {determinante3x3}\u001b[0m')
        input('[ENTER] para continuar...')
        print('\n')
        from main import menuPrincipal
        menuPrincipal()
    else:
        print('Não é possível fazer determinante com essa matriz!')
#Achando o determinante da Matriz caso ela seja 3x3.


#Def de Matriz transposta.
def matrizTransposta():
    matrizPrincipalTransposta = []


    novaQuantColunas = len(matrizPrincipal)
    novaQuantLinhas = len(matrizPrincipal[0])

    matriz_linhas = novaQuantLinhas
    matriz_colunas = novaQuantColunas
    matcontrol = 0


    for quantLinhas in range(0, matriz_linhas):
        matrizPrincipalTransposta.append(0)
        matrizMenor = []
        for c in range(0, matriz_colunas):
            matrizMenor.append(0)
        matrizPrincipalTransposta[matcontrol] = matrizMenor
        matcontrol += 1


    mostrarMatriz(matrizPrincipal)


    for l in range(0, novaQuantLinhas):
        for c in range(0, novaQuantColunas):
            matrizPrincipalTransposta[l][c] = matrizPrincipal[c][l]
    

    mostrarMatriz(matrizPrincipalTransposta)
    
    input('[ENTER] para continuar...')
    print('\n')
    from main import menuPrincipal
    menuPrincipal()


def criarMatrizMult():
    if matrizMult != []:
        opdel = input('Deseja continuar? a matriz existente será deletada!\n(S) para continuar: ')
        if opdel == 'S' or opdel == 's':
            matrizMult.clear()
            print('\n \033[0;32mMatriz Excluida com sucesso!\u001b[0m \n')
            saveDb(matrizMult, filePrincipal)
        else:
            menuMatrizPrincipal()
    matriz_linhas = int(input('Quantidade de linhas: '))
    matriz_colunas = int(input('Quantidade de colunas: '))
    matcontrol = 0


    for quantLinhas in range(0, matriz_linhas):
        matrizMult.append(0)
        matrizMenor = []
        for c in range(0, matriz_colunas):
            matrizMenor.append(0)
        matrizMult[matcontrol] = matrizMenor
        matcontrol += 1


    mostrarMatriz(matrizMult)


    for linha in range(0, matriz_linhas):
        for coluna in range(0, matriz_colunas):
            print(f'Linha[{linha}] Coluna[{coluna}]:')
            matrizMult[linha][coluna] = float(input(f'Digite valor para {linha, coluna}: '))
            mostrarMatriz(matrizMult)
    saveDb(matrizMult, fileMult)
    menuMatrizPrincipal()
    

def multiplicacaoM():
    if matrizMult != [] and matrizPrincipal != []:
        print('='*55)
        print('Matriz principal: ')
        mostrarMatriz(matrizPrincipal)
        print('Matriz Mult: ')
        mostrarMatriz(matrizMult)
        if len(matrizPrincipal[0]) == len(matrizMult):
            print('\033[0;32mÉ possivel fazer a mult!\u001b[0m')

            matrizMultiplicada = [] #Matriz resultado da mult.


            novaQuantLinhas = len(matrizPrincipal) #Dados da nova matriz (matrizMultiplicada) num de linhas da 1º
            novaQuantColunas = len(matrizMult[0]) #Dados da nova matriz (matrizMultiplicada) num de colunas da 2º

            matriz_linhas = novaQuantLinhas
            matriz_colunas = novaQuantColunas
            matcontrol = 0


            for quantLinhas in range(0, matriz_linhas):
                matrizMultiplicada.append(0)
                matrizMenor = []
                for c in range(0, matriz_colunas):
                    matrizMenor.append(0)
                matrizMultiplicada[matcontrol] = matrizMenor
                matcontrol += 1


            mostrarMatriz(matrizMultiplicada)


            mostrarMatriz(matrizMultiplicada)
            input('[ENTER] para continuar...')

        else:
            print('\033[0;91mNão é possivel fazer a multiplicação!\u001b[0m')
        print('='*55)
    if matrizPrincipal == [] and matrizMult == []:
        print('\033[0;32mMatriz que multiplicará e Matriz Principal não foram criadas ainda!\u001b[0m')
    if matrizMult == []:
        print('\033[0;32mMatriz que multiplicará não foi criada ainda!\u001b[0m')
    if matrizPrincipal == []:
        print('\033[0;32mMatriz Principal não foi criada ainda!\u001b[0m')