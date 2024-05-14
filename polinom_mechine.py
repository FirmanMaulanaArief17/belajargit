import math

a = 8
b = 5
theta = math.radians(45)  # konversi sudut ke dalam radian

# Menghitung hasil perkalian a dan b
ab = a * b

# Menghitung nilai cos(θ) dan membulatkannya menjadi 3 angka di belakang koma
cos_theta = round(math.cos(theta), 3)

# Menghitung hasil akhir
hasil = ab * cos_theta

# Menampilkan hasil
print("Menghitung a⃗ . b⃗ ketika sudut antara a⃗ dan b⃗ adalah 45°")
print("Diketahui:")
print("|a⃗| =", a)
print("|b⃗| =", b)
print("θ =", round(math.degrees(theta)), "derajat")
print("\nMaka:")
print("a⃗ . b⃗ = |a⃗| x |b⃗| x cos(θ)")
print("          = {} x {} x {}".format(a, b, cos_theta))
print("          = {}".format(hasil))
