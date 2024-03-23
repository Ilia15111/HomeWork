def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_gcd(b, a % b)
        return d, y, x - (a // b) * y

def find_inverse_element(a, n):
    d, x, y = extended_gcd(a, n)
    if d == 1:
        return x % n
    else:
        return None

a = int(input("Число а: "))
n = int(input("Число n: "))
inverse_element = find_inverse_element(a, n)
if inverse_element is not None:
    print(inverse_element)
else:
    print(f"Обратного элемента к числу {a} по модулю {n} не существует")
