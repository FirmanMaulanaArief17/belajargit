print("="*25)
print("Mengecek Palindrom")
print("="*25)

x = input("Masukkan Kata: ").strip().upper().lower()
w = ""
for i in range(len(x)-1,-1,-1):
   w += x[i]
if ( x == w):
    print("Palindrom")
else :
    print("Bukan Palindrom")