from Verifica_Primo import Fermat, is_prime_MR
from Pseudo_Aleatorio import Blum_Blum_Shub, linear_congruential_generator, lista_bits
from multiprocessing import Process
from random import randint
from time import time

NOME_ARQUIVO = "tabela_tempo.txt"
# "           Algoritmo             |  Numero de Bits   |   Tempo para gerar   |    Numero primo gerado\n"
def Escreve(Algo, N_bits, Tempo, Num_primo):
    unidade = " ms"
    if Tempo > 1000000:
        Tempo /= 1000000
        unidade = " s "
    Algoritmo = f" {Algo}"+" "*(32-len(Algo))
    Num_de_Bits = f"| {N_bits}"+" "*(18-len(str(N_bits)))
    tempo_gerado = "| {:.4f} ".format(Tempo)+unidade+" "*(17-len("{:.4f}".format(Tempo)))
    numero_primo = f"| {Num_primo}"
    with open(NOME_ARQUIVO,'a') as arquivo:
        arquivo.write(Algoritmo+Num_de_Bits+tempo_gerado+numero_primo+"\n")

def Processo(bits, j, h): # Divide o processamento (cada processo testa com um número de bits)
    teste = False
    tempo = time()
    while not teste:
        primo = int([Blum_Blum_Shub(bits), linear_congruential_generator(bits)][j],2)
        print(f"Testa número {primo} com ",["Miller-Rabin","Fermat"][h])
        teste = [is_prime_MR(primo,20), Fermat(primo,2)][h]
    Escreve(["Miller-Rabin","Fermat"][h], bits, (time()-tempo)*1000000, primo)

j = 1 # 0 para Blum Blum Shub | 1 para linear congruential generator
h = 0 # 0 para Miller-Rabin | 1 para Fermat

if __name__ == "__main__":
    with open(NOME_ARQUIVO,'w') as arquivo:
        arquivo.write("           Algoritmo             |  Numero de Bits   |   Tempo para gerar   |    Numero primo gerado\n")
    lista_process = []
    for bits in [40, 56, 80, 128]:#, 168, 224, 256, 512, 1024, 2048, 4096]:
        lista_process.append(Process(target=Processo, args=(bits, j, 0)))
        lista_process[-1].start()
        lista_process.append(Process(target=Processo, args=(bits, j, 1)))
        lista_process[-1].start()
    
    for process in lista_process:
        process.join()
