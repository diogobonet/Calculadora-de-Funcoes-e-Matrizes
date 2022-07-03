import matplotlib.pyplot as plt
import numpy as np


# Opção (Calcular raízes)
def deltafunc(a,b,c):
    delta = (b**2) - (4*a*c)
    print ("O valor de delta(△) é: ",delta)
    if delta < 0:
        print('Essa função não apresenta uma raiz real')
    elif delta == 0:
        print('Essa função apresenta uma raiz real! [x1 = x2]')
    return (delta)
    
#Raizes
def raizes(a,b,c,delta):
    x1 = (-b+ delta**(1.0/2.0)) / (2.0*a)
    x2 = (-b- delta**(1.0/2.0)) / (2.0*a)
    print('='*30)
    print ('O valor de x1 é: {:.2f}' .format(x1), '| O valor de x2 é: {:.2f}' .format(x2))
    return [x1,x2]


# Opção (Calcular função em x pedido)
def funcX(a,b,c):
    print('='*30)
    x = int(input('Digite o valor de X: '))
    y = a*(x**2) + (b*x) + (c)
    print(f"f({x})= ", y) 

# Opção (Calcular Vértice) 
def vertices(a,b,delta):
    xv = (-(b))/ (2.0*a)
    yv = (-(delta))/ (4.0*a)
    print('='*30)
    if a > 0:
        print('O valor mínimo do vértice Xv é:',xv, '| O valor mínimo do vértice Yv é:',yv )
    if a < 0:
        print('O valor máximo do vértice Xv é:',xv, '| O valor máximo do vértice Yv é:',yv )
    return {"Xv":xv,"Yv":yv}

# Opção mostrar gráfico
def grafico(a,b,c,x1,x2):
    eixo_x = []
    eixo_y = []
    zero = []

    plt.ylabel('Valores de Y')
    plt.xlabel('Valores de X')

    variacao = abs(x1 - x2)
    if variacao < 3:
            variacao = 3

    for x in np.arange(x1 - variacao, x2 + variacao, variacao / 100):
        y= a * (x ** 2 ) + b * (x) + c
        eixo_x.append(x)
        eixo_y.append(y)
        zero.append(0.0)
    plt.plot(eixo_x,eixo_y,color="blue")
    plt.plot(eixo_x,zero,color="black")
    plt.show()

def InputABCdelta():
    print('='*30)
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))
    delta = deltafunc(a, b, c)
    print('='*30)
    return [a, b, c, delta, True]


def menuFuncoesSegundoGrau():
    contadorGraf = 0

    ResultABCdelta = InputABCdelta()
    a = ResultABCdelta[0]
    b = ResultABCdelta[1]
    c = ResultABCdelta[2]
    delta = ResultABCdelta[3]
    while True:
        print("\n\033[0;33m[ 1 ] | Calcular Raizes")
        print("[ 2 ] | Calcular Função")
        print("[ 3 ] | Calcular Vértice")
        print("[ 4 ] | Gerar Gráfico")
        print("\033[31m[ 5 ] | Sair")

        op = input("\033[0;0m-> ")
       
        if op == "1":
            listaRaiz = raizes(a, b, c, delta)
            x1 = listaRaiz[0]
            x2 = listaRaiz[1]
            contadorGraf += 1
        elif op == "2":
            funcX(a, b, c)
        elif op == "3":
            vertices(a, b, delta)
        elif op == "4":
            if contadorGraf > 0:
                grafico(a, b, c, x1, x2)
            else:
                print('\033[0;91mFavor calcular primeiro os valores de X1 e X2 na primeira opção [1]!!\033[0;0m')
        elif op == "5":
            break
        else:
            print("\n\033[0;91mValor Inválido! Tente novamente!")
            menuFuncoesSegundoGrau()