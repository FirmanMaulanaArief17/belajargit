kali=2 # global scope

def kuadrat(angka):
    hasil = angka ** kali
    print(f'{angka} pangkat {kali} adalah {hasil}')

angka = int(input("masukan angka : "))
kuadrat(angka)