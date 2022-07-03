# Calculadora de Funções e Matrizes  - Alunos Diogo Sobezak, Eduardo Mussi e Gabriel Mocellin
import matplotlib.pyplot as plt
from CriarMatrizDef import menuMatrizPrincipal
import FuncaoSegundo

# Menu Principal
print("="*55)
print("                     Calculadora")
print("="*55)

def menuPrincipal():
    while True:
        print("\n\033[0;33m[ 1 ] | Função de Segundo Grau")
        print("[ 2 ] | Funções Exponenciais")
        print("[ 3 ] | Matrizes")
        print("\033[31m[ 4 ] | Sair")
        op = input("\033[0;0m-> ")
       
        if op == "1":
            FuncaoSegundo.menuFuncoesSegundoGrau()
        if op == "2":
            funcaoexponencial()
        if op == "3":
            menuMatrizPrincipal()
        if op == "4":
            print("\033[0;91mSaindo...\033[0;0m")
            break
        else:
            menuPrincipal()
    return None
            

def funcaoexponencial():
    print("\033[0;97m="*55)
    print("\033[0;94m                  Função Exponencial")
    print("\033[0;97m="*55)
    try:
        valueA = float(input("Valor A: "))
        valueB = float(input("Valor B: "))
    except:
        print("\033[31mOs valores A e B deveram ser apenas números!\033[0;0m")
        return funcaoexponencial()
    print("\n\033[0;33m[ 1 ] | Verificar (Crescente ou Decrescente)")
    print("[ 2 ] | Calcular função em x pedido")
    print("[ 3 ] | Gerar gráfico")
    print("\033[31m[ 4 ] | Voltar para o menu\033[0;0m")
    if valueA == 0 or valueB == 0:
        print("\033[31mO valor não pode ser igual a 0!\033[0;0m")
        return funcaoexponencial()
    try:
        while True:
            op = input("\n\033[0;0m-> ")
            if op == "1":
                if valueA >= 1:
                    print("\033[0;32mCrescente!\033[0;0m")
                if valueA <= 0 or valueA < 1:
                    print("\033[0;91mDecrescente!\033[0;0m")
                    funcaoexponencial()
            elif op == "2":
                valorX = float(input("Valor de X: "))
                if valorX == 0:
                    print("Valor inválido! Tente novamente!")
                    funcaoexponencial()
                else:
                    y = valueA * (valueB ** valorX)
                    print(f"f({valorX}) = {y}")
                    return funcaoexponencial()
            elif op == "3":
                plt.plot(valueA, valueB)
                plt.show()
                funcaoexponencial()
            elif op == "4":
                menuPrincipal()
            else:
                print("\033[31mTente novamente!\033[0;0m")
    except ValueError:
        print("\033[31mTente novamente!\033[0;0m")
# Rodar o code
menuPrincipal()