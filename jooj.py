import math

def Sassenfeld(A):
    coeficientes = []
    for i in range(len(A)):
        b = 0
        for j in range(len(A)):
            if (i != j and i == 0) or i < j:
                b += A[i][j]
            elif i != j and i != 0:
                b += A[i][j]*coeficientes[j]
        b /= A[i][i]
        coeficientes.append(b)
    maiorCoeficiente = max(coeficientes)
    if maiorCoeficiente < 1:
        print('O metodo de Gauss-Seidel irá convergir')
        return True
    else:
        print('O metodo de Gauss-Seidel não irá convergir')
        return False


def findError(vOld, vNew):
    vDiff = []
    for i in range(len(vOld)):
        Diff = abs(vNew[i] - vOld[i])
        vDiff.append(Diff)
    output = max(vDiff)/abs(max(vNew))
    return output


def GaussSeidel(A,b,vSol,stop,n):
    iteracao = 0
    criteria = Sassenfeld(A)
    while iteracao < n and criteria:
        vAux = []
        for value in vSol:
            vAux.append(value)
        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if i != j:
                    x -= A[i][j]*vSol[j]
            x /= A[i][i]
            vSol[i] = x
        iteracao += 1
        error = findError(vAux, vSol)
        body = f'iteração numero {iteracao}: '
        for number in vSol:
            body += ' ' + str(number) + ','
        body += f' com erro de {error}'
        if error < stop:
            criteria = False
            body += '\n Precisão exigida atingida, cessando...'
        print(body)

A = [[8,2,-1,0],[2,-4,0,0],[0,-2,8,-1],[0,0,-1,4]]
b = [1,1,1,1]
SolucaoInicial = [0,0,0,0]
MargemErro = 0.0000001
nIteracoes = 5

GaussSeidel(A,b,SolucaoInicial, MargemErro, nIteracoes)
