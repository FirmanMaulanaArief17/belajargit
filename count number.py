nim = input('no: ')
angka = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
angka = 0
for x in nim:
    if x in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
        angka += 1
print(angka)