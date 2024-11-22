A = {1, 4, 7, 10} 

B = set()

for x in A:
    for y in A:
        if x != y:
            B.add(abs(x - y))


print("Множина B (відстані між точками):", B)