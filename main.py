print("Ляшенко Илья Денисович")
print("090304-РПИа-о23")

a = int(input("Введите число a: "))
n = int(input("Введите число n: "))

def mod(a,b,n):
    r = a*b
    while (r>n):
        r-=n
    return r 
    
b = 0
r = mod(a,b,n)
while(r != 1):
    b+=1
    r = mod(a,b,n)
print(f"Значение b = {b}")