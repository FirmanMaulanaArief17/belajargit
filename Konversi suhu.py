print("="*36) 
print("Celcius", "Fahrenheit", "Reamur", "Kelvin", sep=" ")
def pjg(x):
        s=str(x)
        return len(s)
for x in range(0, 101, 10):
        y=int(x*(9/5)+32)
        z=int(x*(4/5))
        a=x+273.15
        print(x, " "*(9-pjg(x)), y, " "*(12-pjg(y)), z," "*(8-pjg(z)), a,sep="")
        print("="*36)