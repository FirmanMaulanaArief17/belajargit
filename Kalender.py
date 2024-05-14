# Mengimpor Modul Calendar
import calendar
# Menginput Tahun dan Bulan
yy = int(input("Masukkan Tahun: "))
mm = int(input("Masukkan Bulan: "))
# Menampilkan kalender bulanan
print(calendar.month(yy, mm))