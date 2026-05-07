# Повороты
p0 = [1,2,3,4,5,6]
p1 = [2,3,4,5,6,1]
p2 = [3,4,5,6,1,2]
p3 = [4,5,6,1,2,3]
p4 = [5,6,1,2,3,4]
p5 = [6,1,2,3,4,5]

# Отражения
s1 = [1,6,5,4,3,2]
s2 = [2,1,6,5,4,3]
s3 = [3,2,1,6,5,4]
s4 = [4,3,2,1,6,5]
s5 = [5,4,3,2,1,6]
s6 = [6,5,4,3,2,1]

G = [p0,p1,p2,p3,p4,p5,s1,s2,s3,s4,s5,s6]
name = ["e","a","a2","a3","a4","a5","b1","b2","b3","b4","b5","b6"]

def mul(x, y):
    result = [0 for _ in range(6)]
    k = 0
    while k < 6:
        result[k] = x[y[k] - 1]
        k = k + 1
    return result

def find(p):
    index = 0
    while index < 12:
        if G[index] == p:
            return name[index]
        index = index + 1
    return "?"

print("   ", " ".join(name))
i = 0
while i < 12:
    row_list = []
    j = 0
    while j < 12:
        row_list.append(find(mul(G[i], G[j])))
        j = j + 1
    print(name[i], " ".join(row_list))
    i = i + 1

print("\nПорядок группы: 12")

is_abelian = True
i = 0
while i < 12:
    j = 0
    while j < 12:
        if mul(G[i], G[j]) != mul(G[j], G[i]):
            is_abelian = False
            break
        j = j + 1
    if is_abelian == False:
        break
    i = i + 1

if is_abelian == True:
    print("Группа абелева")
else:
    print("Группа не абелева")