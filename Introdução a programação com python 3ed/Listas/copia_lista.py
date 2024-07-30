l = [1,2,3,4,5]
v = l[:] #referencia uma copia de L

print(l)
print(v)

v[0] = 6
print(l)
print(v)
