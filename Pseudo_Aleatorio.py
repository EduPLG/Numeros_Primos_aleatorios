import random
import time

def Blum_Blum_Shub(num_bits):
    """
    Referência: https://www.gkbrk.com/wiki/blum-blum-shub/
    """
    P = random.randint(23, 1237893)
    Q = random.randint(29, 1238277)
    M = P * Q
    seed = random.randint(127, 128399)
    bit = ""
    for i in range(num_bits):
        seed = (seed * seed) % M # somatório (x² mod M) num_bits vezes 
        bit += str(seed & 1) # 1 se for ímpar; 0 se for par
    return bit


def linear_congruential_generator(n_bits):
    """
    Referência: https://github.com/rossilor95/lcg-python/blob/main/lcg.py
    """
    x = random.randint(3084, 608435)
    m = 0
    while not (m%2): # enquanto m for par
        m = random.randint(13, x)
    a, c = random.randint(13,x), random.randint(13,x)
    bits = ""
    for i in range(n_bits):
        x = (a * x + c) % m
        bits += str(x & 1)
    return bits


# Blum_Blum_shub| linear_congruential_generator
# tempo tempo
tabela = [[],[]]
lista_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

for bits in lista_bits:
    for j in range(2):
        media = 0
        for i in range(10):
            val = time.time()
            [Blum_Blum_Shub(bits), linear_congruential_generator(bits)][j]
            media += time.time()-val
        tabela[j].append(media/10)


print("  Bits   |   Blum_Blum_Shub    |  linear_congruential_generator")
for bits,i,j in zip(lista_bits, tabela[0], tabela[1]):
    print("--"*30)
    print(" ", bits, "    |  ", "   {:.8f} ms  ".format(i*1000), " | ", "   {:.8f} ms".format(j*1000))
