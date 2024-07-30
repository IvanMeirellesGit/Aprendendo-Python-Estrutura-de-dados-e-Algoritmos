L = []

while True:
    n = int(input("Digite um numero. (0 sai): "))
    if n == 0:
        break
    L.append(n)

i = 0
while i < len(L):
    print(L[i])
    i+=1
