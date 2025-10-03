import datetime
import os

start = datetime.datetime.now()
os.system('clear')

################################################################################

class MT19937:
    def __init__(self, seed: int = 5489):
        # Parâmetros do MT19937 (32 bits)
        self.N = 624
        self.M = 397
        self.MATRIX_A   = 0x9908B0DF
        self.UPPER_MASK = 0x80000000  # bit alto (MSB)
        self.LOWER_MASK = 0x7FFFFFFF  # 31 bits baixos (LSB)

        self.state = [0] * self.N
        self.idx = self.N  # força twist antes da 1ª extração
        self.seed(seed)

    def seed(self, seed: int):
        """Inicializa o estado a partir de uma semente de 32 bits."""
        self.state[0] = seed & 0xFFFFFFFF
        for i in range(1, self.N):
            x = self.state[i-1]
            self.state[i] = (1812433253 * (x ^ (x >> 30)) + i) & 0xFFFFFFFF
        self.idx = self.N

    def _twist(self):
        """Atualiza o bloco completo de estado (twist)."""
        for i in range(self.N):
            y = (self.state[i] & self.UPPER_MASK) | (self.state[(i+1) % self.N] & self.LOWER_MASK)
            self.state[i] = (self.state[(i + self.M) % self.N] ^
                              (y >> 1) ^
                              (self.MATRIX_A if (y & 1) else 0)) & 0xFFFFFFFF
        self.idx = 0

    def rand_uint32(self) -> int:
        """Retorna um inteiro não-negativo de 32 bits (uint32)."""
        if self.idx >= self.N:
            self._twist()

        x = self.state[self.idx]
        self.idx += 1

        # Tempering
        y = x ^ (x >> 11)
        y ^= (y << 7)  & 0x9D2C5680
        y ^= (y << 15) & 0xEFC60000
        y ^= (y >> 18)
        return y & 0xFFFFFFFF

    def random(self) -> float:
        """
        Retorna float em [0,1). Constrói ~53 bits de precisão (como CPython):
        usa 27 bits + 26 bits de duas saídas de 32 bits.
        """
        a = self.rand_uint32() >> 5   # 27 bits
        b = self.rand_uint32() >> 6   # 26 bits
        return (a * 67108864.0 + b) / 9007199254740992.0  # 2^26 * 2^27 / 2^53

    def uniform(self, low: float = 0.0, high: float = 1.0) -> float:
        """Uniforme contínua em [low, high)."""
        return low + (high - low) * self.random()

    def randint(self, a: int, b: int) -> int:
        """
        Inteiro uniforme em [a, b] sem viés (rejeição).
        Evita o viés de (rand_uint32() % range).
        """
        if a > b:
            raise ValueError("Intervalo inválido: a > b")
        span = b - a + 1
        # Maior múltiplo de span que cabe em 2^32 para rejeição
        limit = (1 << 32) - ((1 << 32) % span)
        while True:
            r = self.rand_uint32()
            if r < limit:
                return a + (r % span)

################################################################################

print("--------------------------------------------------------------")
print("Geração de números pseudoaleatórios usando o Mersenne Twister")
print("--------------------------------------------------------------")

mt = MT19937(seed=5489)

print(f'Semente: {mt.state[0]}'+'\n')

seq = []    
for i in range(15):
    Xn = mt.rand_uint32()
    Un = Xn / 2**32
    print(f'X{i+1} = {Xn:10d}  U{i+1} = {Un:.10f}')
    seq.append(Un)

print("\nSequência gerada:", seq)


# 3 floats em [0,1)
#print(mt.random(), mt.random(), mt.random())

# Inteiro uniforme em [10, 20]
#print(mt.randint(10, 20))

# Uniforme contínua em [5.0, 7.5)
#print(mt.uniform(5.0, 7.5))

################################################################################

end = datetime.datetime.now()
time = end - start
print(f'Tempo total de execução: {time}')

################################################################################