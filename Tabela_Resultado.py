from Verifica_Primo import Fermat, is_prime_MR
from Pseudo_Aleatorio import Blum_Blum_Shub, linear_congruential_generator, lista_bits
from multiprocessing import Process, Lock
from random import randint
from time import time


# "   Algoritmo    |   Bits   |   Tempo para gerar   |    Numero primo gerado\n"
def Escreve(Algo, N_bits, Tempo, Num_primo):
    unidade = " ms "
    if Tempo > 1000000:
        Tempo /= 1000000
        unidade = " s  "
    Algoritmo = f" {Algo}"+" "*(15-len(Algo))
    Num_de_Bits = f"| {N_bits}"+" "*(9-len(str(N_bits)))
    tempo_gerado = "|"+" "*(17-len("{:.4f}".format(Tempo)))+"{:.4f} ".format(Tempo)+unidade
    numero_primo = f"| {Num_primo}"
    with open("tabela_tempo.txt",'a') as arquivo:
        arquivo.write(Algoritmo+Num_de_Bits+tempo_gerado+numero_primo+"\n")

def Processo(lock, bits, j, h): # Divide o processamento (cada processo testa com um número de bits)
    teste = False
    tempo = time()
    while not teste: # Enquanto não aceitar como primo
        primo = int([Blum_Blum_Shub(bits)[:-1]+"1", linear_congruential_generator(bits)[:-1]+"1"][j],2) # pega um número
        teste = [is_prime_MR(primo,10), Fermat(primo,10)][h] # Testa se é primo
    tempo = (time()-tempo)*1000000
    with lock: # Para dois processos não tentarem escrever ao mesmo tempo
        Escreve(["Miller-Rabin","Fermat"][h], bits, tempo, primo)


if __name__ == "__main__":
    Tempo_total = time()
    with open("tabela_tempo.txt",'w') as arquivo:
        arquivo.write("   Algoritmo    |   Bits   |   Tempo para gerar   |    Numero primo gerado\n")
    lock = Lock()
    lista_process = []
    for bits in [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]:
        lista_process.append(Process(target=Processo, args=(lock, bits, randint(0,1), 0))) # Miller-Rabin
        lista_process[-1].start() # randint(0,1) -> 0 para Blum Blum Shub | 1 para linear congruential generator
        lista_process.append(Process(target=Processo, args=(lock, bits, randint(0,1), 1))) # Fermat
        lista_process[-1].start() # randint(0,1) -> 0 para Blum Blum Shub | 1 para linear congruential generator
    
    input("Aperte ENTER para terminar") # Para quando quiser parar e ver por quanto tempo rodou
    for process in lista_process:
        if process.is_alive():
            process.terminate()
    Tempo_total = time() - Tempo_total
    with open("tabela_tempo.txt",'a') as arquivo:
        arquivo.write("\nPrograma executou por {} min e {:.4} s\n".format(int(Tempo_total//60), Tempo_total%60))
