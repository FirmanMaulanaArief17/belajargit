def fahrenheit(x):
    f = (int(x) * (9/5)) + 32
    return str(str(f) + '°F')
def reamur(x):
    r = float(x) * 0.8
    return str(str(r) + '°R')
def kelvin(x):
    k = float(x) + 273.15
    return (str(k) + '°K')
def table():
    t = 0
    while t <= 100:
        print((str(t)+'°C'),fahrenheit(t),reamur(t),kelvin(t))
        t += 10

table()