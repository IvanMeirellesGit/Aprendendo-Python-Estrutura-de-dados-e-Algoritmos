T = [-10, -8, 0, 1, 2, 5, -2, -4]

temp_min = T[0]
temp_max = T[0]
media = 0

for e in T:
    if e > temp_max:
        temp_max = e
    if e < temp_min:
        temp_min = e
    media = media + e

print(f"Temperatura minima: {temp_min}")
print(f"Temperatura maxima: {temp_max}")
print(f"Temperatura Média: {media / len(T)}")