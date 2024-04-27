import random

def fyShuffle(array):
    iterations = len(array)

    while iterations:
        iterations = iterations - 1

        ri = random.randint(0, iterations)
        
        t = array[iterations]
        array[iterations] = array[ri]
        array[ri] = t

    return array

if __name__ == "__main__":
    a = list(range(15))
    print(f'array: {a}')
    print(f'randomized: {fyShuffle(a)}')