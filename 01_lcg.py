import datetime
import os

start = datetime.datetime.now()
os.system('clear')

################################################################################

def lcg(m, a, c, x0, n):

    """
    Gera n números pseudoaleatórios usando o método congruencial linear.
    
    Parâmetros:
        m  - módulo
        a  - multiplicador
        c  - incremento
        x0 - semente inicial
        n  - quantidade de números a gerar
    Retorna:
        lista de tuplas (Xn, Un)
    """

    print("--------------------------------------------------------------")
    print("Geração de números pseudoaleatórios usando o método LCG")
    print("--------------------------------------------------------------")
    print(f"m = {m}, a = {a}, c = {c}, x0 = {x0}, n = {n}\n")   

    resultados = []
    x = x0

    u = x / m             
    resultados.append((x, u))

    for _ in range(n):
        x = (a * x + c) % m   # recorrência
        u = x / m             # normalização
        resultados.append((x, u))
    
    print(f"{'n':^6}|{'Xn':^6}|{'Un':^6}")
    print("-"*20)

    for i, (x, u) in enumerate(resultados, start=0):
        print(f"{i:^6}|{x:^6}|{u:^6.6f}")

    print("\nSequência gerada:", [x for x, u in resultados])

    return resultados

################################################################################

# Exercício 1
m = 9; a = 2; c = 1; x0 = 1; n = 15  

# Exercício 2
#m = 10; a = 7; c = 7; x0 = 1; n = 15  

# Exercício 3 - Park & Miller (1988)
#m = 2**31-1; a = 7**5; c = 0; x0 = 1; n = 15  

seq = lcg(m, a, c, x0, n)

################################################################################

end = datetime.datetime.now()
time = end - start
print(f'Tempo total de execução: {time}')

################################################################################