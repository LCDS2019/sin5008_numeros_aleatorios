import datetime
import os

start = datetime.datetime.now()
os.system('clear')

################################################################################
def lcg_schrage(x0, a=16807, m=2147483647, n=10):
    """
    Gera n números pseudoaleatórios usando LCG com algoritmo de Schrage.
    Corrigido: nunca retorna números negativos.
    """

    print("--------------------------------------------------------------")
    print("Geração de números pseudoaleatórios usando o método de Schrage")
    print("--------------------------------------------------------------")
    print(f"m = {m}, a = {a}, x0 = {x0}, n = {n}\n")  

    q = m // a
    r = m % a
    x = x0
    seq = []
    for _ in range(n):
        x = a * (x % q) - r * (x // q)
        while x <= 0:
            x += m   # <-- ajuste para evitar negativos

        u = x / m             # normalização
        seq.append((x, u))

    print(f"{'n':^6}|{'Xn':^6}|{'Un':^6}")
    print("-"*20)

    for i, (x, u) in enumerate(seq, start=1):
        print(f"{i:^6}|{x:^6}|{u:^6.6f}")

    print("\nSequência gerada:", [x for x, u in seq])

    return seq

################################################################################

# Exercício 1
m = 19; a = 7; x0 = 16; n = 15  

# Exercício 2
#m = 10; a = 7; c = 7; x0 = 1; n = 15  

# Exercício 3 - Park & Miller (1988)
#m = 2**31-1; a = 7**5; c = 0; x0 = 1; n = 15  

seq = lcg_schrage(x0,a,m, n)

################################################################################

end = datetime.datetime.now()
time = end - start
print(f'Tempo total de execução: {time}')

################################################################################