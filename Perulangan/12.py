# Jika kita gabungkan for ... else dengan break, 
# maka blok else hanya akan dieksekusi jika perintah break tidak dieksekusi.
# Kita bisa memanfaatkan for ... else + break untuk pencarian sebuah item pada list.

listKota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta', 'Semarang', 'Makassar'
]

kotaYangDicari = input('Ketik nama kota yang kamu cari: ')

for i, kota in enumerate(listKota):
  # kita ubah katanya ke lowercase agar 
  # menjadi case insensitive
  if kota.lower() == kotaYangDicari.lower():
    print('Kota yang anda cari berada pada indeks', i)
    break
else:
  print('Maaf, kota yang anda cari tidak ada')