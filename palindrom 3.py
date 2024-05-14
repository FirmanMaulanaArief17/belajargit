n = int(input("Masukkan angka: "))

def is_dec_bin_palindrome(n):
    t=str(n)
    if t != t[::-1]:
        return False
    b=bin(n)[2:]
    print(b)
    return b==b[::-1]

print(is_dec_bin_palindrome(n))