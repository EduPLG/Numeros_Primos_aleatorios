import random
import time

def Blum_Blum_Shub(num_bits):
    """
    Referência: https://www.gkbrk.com/wiki/blum-blum-shub/
    """
    M = random.randint(29, 9999999)
    seed = random.randint(13, M-1)
    bit = ""
    for _ in range(num_bits):
        seed = (seed * seed) % M # somatório (x² mod M) num_bits vezes O(n²)
        bit += str(seed & 1) # 1 se for ímpar; 0 se for par
    return bit


def linear_congruential_generator(n_bits):
    """
    Referência: https://github.com/rossilor95/lcg-python/blob/main/lcg.py
    """
    m = random.randint(29, 9999999)
    x = random.randint(13, m-1)
    a, c = random.randint(13,m-1), random.randint(13,m-1)
    bits = ""
    for _ in range(n_bits):
        x = (a * x + c) % m # somatório a*x +c mod M num_bits vezes O(n)
        bits += str(x & 1)
    return bits


lista_bits = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

if __name__ == '__main__':
    tabela = [[],[]]
    # Cria um número pseudo aleatório e guarda o tempo na lista tabela 0 para BlumBlumShub e 
    # 1 para linear_congruential_generator
    for bits in lista_bits: # número de bits do número
        for j in range(2): # Para testar os dois geradores
            media = 0
            for _ in range(1000): # 1000 tentativas para cada gerador
                val = time.time()*1000 # seria 1.000.000 mas como vai dividir por 1.000 na média
                [Blum_Blum_Shub(bits), linear_congruential_generator(bits)][j]
                media += (time.time()*1000-val) # seria 1.000.000 mas como vai dividir por 1.000 na média
            tabela[j].append(media)

    print("  Bits     |   Blum_Blum_Shub    |  linear_congruential_generator")
    for bits,i,j in zip(lista_bits, tabela[0], tabela[1]):
        print("--"*30)
        print(" ", bits, " "*(5-len(str(bits)))," |  ", "   {:.8f} ms  ".format(i), " | ", "   {:.8f} ms".format(j))
    print()
