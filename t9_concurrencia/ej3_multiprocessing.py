import multiprocessing
import time

NUM_PROCESOS = 3
ITERACIONES = 3
N = 100_000_000


def suma_enesima(n):
    """
    Suma todos los números del cero a n.

    :param n: El límite superior de números a sumar
    :return: La suma de todos los números del 0 a n
    """
    suma_total = sum(range(n + 1))
    return print("Suma: " + str(suma_total))


def sin_multiprocessing():
    print("Iniciando función sin multiprocessing.")
    for _ in range(ITERACIONES):
        suma_enesima(N)


def con_multiprocessing():
    print("Iniciando función con multiprocessing.")

    trabajos = [
        multiprocessing.Process(target=suma_enesima, args=(N,))
        for _ in range(NUM_PROCESOS)
    ]

    # Iniciar cada proceso
    for trabajo in trabajos:
        trabajo.start()

    # Esperar a que todos los procesos terminen
    for trabajo in trabajos:
        trabajo.join()


def main():
    print("Sumando todos los números entre 0 y " + str(N) + ".\n")

    start_time = time.time()
    sin_multiprocessing()
    print(
        "--- La función sin multiprocessing tomó %s segundos ---\n"
        % (time.time() - start_time)
    )

    start_time = time.time()
    con_multiprocessing()
    print(
        "--- La función con multiprocessing tomó %s segundos ---"
        % (time.time() - start_time)
    )


if __name__ == "__main__":
    main()
