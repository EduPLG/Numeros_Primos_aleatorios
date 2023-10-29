from Pseudo_Aleatorio import Blum_Blum_Shub, linear_congruential_generator, lista_bits
from random import randint
from time import time


def is_prime_MR (n: int, t: int) -> bool:
    """
    Referência: https://herrmann.tech/pt/blog/2021/11/23/meu-primeiro-codigo-python-14-anos-depois.html#:~:text=O%20Miller-Rabin%20é%20um,apenas%20um%20de%20vários%20erros.
    
    E

    https://www.youtube.com/watch?v=qdylJqXCDGs
    

    :return: False se o número é composto, True se primo ou pseudoprimo
    :rtype: bool
    """
    if n == 1: return False # Caso o número pseudoaleatório gerado == 0
    if (n % 2 == 0): return False # Para quando o número for muito pequeno (pode dar erro)
    r = n - 1
    s = 0
    while (r % 2 == 0): # Procura o valor de s e r para -> n-1 = 2**s * r 
        """
        Começa dividindo n-1 por potências de 2 até a divisão não ser mais inteira,
        com o valor da divisão sendo o r e s a potência de dois, pode continuar
        """
        s = s + 1
        r = r // 2
    for i in range(t):
        a = randint(2, n - 2) # a aleatório maior que 1 e menor que n-1
        y = pow (a, r, n)               # a**r % n
        if (y != 1) and (y != n - 1): # verifica se o resultado é diferente de 1 e (-1 mod n) -> (n-1)
            """
            Caso seja diferente, é preciso verificar se o quadrado desse valor mod n não é 1 ou n-1
            se for 1, significa que ele é um número composto, logo não primo

            se for -1 mod n -> (n-1) é provavelmente primo, sai do loop e passa pra próxima iteração

            se for diferente de 1 e -1, faça o quadrado dele até chegar em 1 ou -1, ou defina um limite e
                                                                            retorne o número como não primo.
            """
            j = 1
            while (j < s) and (y != n - 1): # limite (j) ou se chegou a -1 mod n -> (n-1)
                y = (y * y) % n
                if y == 1: # Com certeza não é primo
                    return False
                j = j + 1
            if y != n - 1:
                return False
    return True


def MDC(a,b):
    i = 0
    while b != 0 and i < 100:
        i += 1
        resto = a % b
        a = b
        b = resto
    return a


def Fermat(n, k):
    """
    Referência: https://www.youtube.com/watch?v=q53TAGBuFAw
    """
    if n == 1: return False # caso o número pseudoaleatório gerado == 0
    if n%2 == 0:
        return False
    elif n == 3: # para que o randint de a tenha possíveis escolhas
        return True
    for _ in range(k):
        a = randint(2, n-1)
        if MDC(n,a) != 1: # Caso n tenha um MDC com a que não seja 1 (num composto)
            return False
        elif pow(a,(n-1),n) != 1: # Caso a**(n-1) mod n não seja 1 (num composto)
            return False
    return True


if __name__ == "__main__":
    for nbits in [40,56, 80, 128]:
        Mr = False
        Fr = False
        while not Mr and not Fr:
            primo = int(linear_congruential_generator(nbits)[:-1]+"1",2) # Retorna num binário com o ultimo bit sempre 1
            Mr = is_prime_MR(primo,5) # Retorna True/False
            #print(f"Miller-Rabin: {primo} ", Mr)
            Fr = Fermat(primo,2) # Retorna True/False
            #print(f"Fermat: {primo} ", Fr)
        print(f"O número {primo} é primo para Miller-Rabin: {Mr}!")
        print(f"O número {primo} é primo para Fermat: {Fr}!")
