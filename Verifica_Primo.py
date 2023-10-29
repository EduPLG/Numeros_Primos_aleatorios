from Pseudo_Aleatorio import Blum_Blum_Shub, linear_congruential_generator, lista_bits
from random import randint
import timeout_decorator


def is_prime_MR (n: int, t: int) -> bool:
    """
    Referência: https://herrmann.tech/pt/blog/2021/11/23/meu-primeiro-codigo-python-14-anos-depois.html#:~:text=O%20Miller-Rabin%20é%20um,apenas%20um%20de%20vários%20erros.
    Verifica se um número é composto ou provavelmente primo,
    usando o teste probabilístico de Miller-Rabin.

    :param int n: O inteiro a ser testado
    :param int t: Parâmetro de segurança, números maiores demoram
                  mais, mas aumentam a probabilidade do número ser
                  primo

    :return: False se o número é composto, True se primo ou pseudoprimo
    :rtype: bool
    """
    if n in [1,2,3]: return True 
    if (n % 2 == 0): return False # Para quando o número for muito pequeno (pode dar erro)
    r = n - 1
    s = 0
    while (r % 2 == 0):
        s = s + 1
        r = r // 2
    for i in range(t):
        a = randint(2, n - 2)
        y = pow (a, r, n)
        if (y != 1) and (y != n - 1):
            j = 1
            while (j < s) and (y != n - 1):
                y = (y * y) % n
                if y == 1:
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
    if n in [1,2,3]: return True 
    if n%2 == 0:
        return False
    elif n == 3:
        return True
    for _ in range(k):
        a = randint(2, n-1)
        if MDC(n,a) != 1:
            return False

        if a**(n-1)%n != 1: 
            return False

    return True


if __name__ == "__main__":
    for nbits in [13,20]:
        Mr = False
        Fr = False
        while not Mr and not Fr:
            primo = int(Blum_Blum_Shub(nbits),2)
            Mr = is_prime_MR(primo,20)
            Fr = Fermat(primo,2)
        print(f"O número {primo} é primo para Miller-Rabin: {Mr}!")
        print(f"O número {primo} é primo para Fermat: {Fr}!")
