# mi_primer_script.py

print("¡Hola, Github!")

def primos_hasta_1000():
    limite = 1000
    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False

    for i in range(2, int(limite ** 0.5) + 1):
        if es_primo[i]:
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False

    primos = [i for i in range(2, limite + 1) if es_primo[i]]
    return primos

# Mostrar los números primos entre 1 y 1000
print(primos_hasta_1000())

