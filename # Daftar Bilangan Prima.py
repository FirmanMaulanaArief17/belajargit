# Daftar Bilangan Prima

lower = int(input("Masukkan batas bawah : "))
upper = int(input("Masukkan batas atas : "))
print("Bilangan prima antara ", lower, "dan ", upper, ":")

for i in range(lower, upper+1):
    if i > 1:
        for n in range(2, i):
            if (i % n) == 0:
                break
        else:
            print(i)