# Matriks m baris x n kolom

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

for i in range(m):
    print(matriks[i])