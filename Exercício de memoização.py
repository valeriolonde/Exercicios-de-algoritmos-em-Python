def memoize(funcao):
    cache = {}

    def funcao_memoizada(*args):
        if args in cache:
            return cache[args]
        else:
            resultado = funcao(*args)
            cache[args] = resultado
            return resultado

    return funcao_memoizada

def add(a, b, c):
    return a + b + c

if __name__ == "__main__":
    new_add = memoize(add)
    print(new_add(1, 2, 3))  # Saída: 6
    print(new_add(1, 2, 3))  # Saída: 6 (Não calculou novamente add(1, 2, 3).)
