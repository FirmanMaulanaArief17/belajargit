def faktorial(n):
    assert n>=1
    if n == 1:
        return 1

    else:
        return n * faktorial(n-1)

print(faktorial(3))