awal = int(input("Masukkan Nilai Awal : "))
akhir = int(input("Masukkan Nilai Akhir : "))

jumlah = 0
total = 0

for a in range(awal,akhir+1):
    print(a, end=" ")
    jumlah = jumlah+1
    total = total+a
print()
print("Bilangan di atas berjumlah :",jumlah)
print("Total bilangan di atas adalah :",total)