x = int(input("Zadaj x: "))
y = int(input("Zadaj y: "))
z = int(input("Zadaj z: "))

if x <= y:
    max = y
else:
    max = x
if z > max:
    max = z
print("najvačšie číislo je",max)