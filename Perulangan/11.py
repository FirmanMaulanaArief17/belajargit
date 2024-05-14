# Perulangan for jika ditambahkan blok else, 
# maka perintah yang ada pada blok else hanya akan dieksekusi ketika perulangan selesai secara natural tanpa interupsi.

listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

for kota in listKota:
  print(kota)
else:
  print('Tidak ada lagi item yang tersisa')