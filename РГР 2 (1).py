from math import gcd

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    return x % m if g == 1 else None

def solve_congruence_system():
    n = int(input("Введите количество сравнений: "))
    residues, moduli = [], []
    
    for i in range(n):
        print(f"\nСравнение №{i + 1}")
        a = int(input("Введите остаток a: "))
        m = int(input("Введите модуль m: "))
        if m <= 0:
            print("Модуль должен быть положительным.")
            return
        residues.append(a)
        moduli.append(m)
    
    x, m = residues[0], moduli[0]
    
    for i in range(1, n):
        g = gcd(m, moduli[i])
        if (residues[i] - x) % g != 0:
            print("\nСистема не имеет решений.")
            return
        
        m1_div = m // g
        m2_div = moduli[i] // g
        diff = (residues[i] - x) // g
        
        inv = mod_inverse(m1_div, m2_div)
        if inv is None:
            print("\nСистема не имеет решений.")
            return
        
        t = (diff * inv) % m2_div
        m = m * m2_div
        x = (x + m // m2_div * t) % m
    
    print(f"\nОтвет: x ≡ {x} (mod {m})")

solve_congruence_system()