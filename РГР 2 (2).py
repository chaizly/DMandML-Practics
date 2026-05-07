from math import gcd

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    return x % m if g == 1 else None

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

phrase = "Четные числа - питательные, а нечетные - просто вкусные"

print("Стандартные значения p = 61, q = 53")
choice = input("Ввести свои p и q? да/нет: ").lower()

if choice == "да":
    p = int(input("Введите простое число p: "))
    q = int(input("Введите простое число q: "))
else:
    p, q = 61, 53

if not is_prime(p) or not is_prime(q) or p == q:
    print("Ошибка: p и q должны быть разными простыми числами.")
else:
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17
    while gcd(e, phi) != 1:
        e += 1
    
    d = mod_inverse(e, phi)
    
    if d is None or n <= 255:
        print("Ошибка при генерации ключей.")
    else:
        print(f"\nИсходная фраза: {phrase}")
        encrypted = [pow(b, e, n) for b in phrase.encode("utf-8")]
        print(f"\nЗашифровано: {encrypted}")
        decrypted = bytes([pow(c, d, n) for c in encrypted]).decode("utf-8")
        print(f"\nРасшифровано: {decrypted}")