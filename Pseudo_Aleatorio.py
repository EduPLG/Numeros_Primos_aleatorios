import random
import time

def Blum_Blum_Shub(seed, M, num_bits):
    bit = ""
    for i in range(num_bits):
        seed = (seed * seed) % M # somatório (x² mod M) num_bits vezes 
        print(seed, end=' ')
        bit += str(seed & 1) # 1 se for ímpar; 0 se for par
    print()
    return bit


P = 23
Q = 29
M = P * Q
seed = random.randint(2, 9)
lista_tempo = []
lista_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

for i in range(10):
    #print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    val = time.time()
    print(Blum_Blum_Shub(seed, M, 50))
    lista_tempo.append(time.time()-val)

print("Bits   |   Blum_Blum_Shub    |  ")
for bits,i in zip(lista_bits, lista_tempo):
    print("---------------------------------------")
    print("   ",bits,"      ",i)