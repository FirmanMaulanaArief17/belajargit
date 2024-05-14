

def fibo(x):

    if x == 0:
        return [x]

    number = fibo(x-1)
    indek = len(number)

    angka1 = number[-2] if indek > 2 else 0
    angka2 = number[-1] if indek > 2 else 1

    return number + [angka1 + angka2]


angka = int(input("masukan angka : "))

print(fibo(angka-1))