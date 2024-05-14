#penjumlahan matriks
m=int(input())
n=int(input())

matriks=[]
for i in range(m):
    row=[]
    for j in range(n):
        if i==j:
            a=1
        else:
            a=0
        row.append(a)
    matriks.append(row)

for i in range(0, len(matriks1)):
    for j in range(0, len(matriks2)):
        print(matriks1[i][j]+matriks2[i][j], end=" "),
    print