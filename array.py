import array as arr

a = arr.array("i", [1, 2, 3])


print("The new created array is:", a, end = "")

for i in range(0, 3):
    print(a[i], end = "")
print()

b = arr.array("d", [2.5, 3.2, 3.3])

print("The new created array is:", a, end = "")
for i in range(0, 3):
    print(b[i], end = "")


a.insert(1, 4)
print("Array after insertion:", end = "")
for i in (a):
    print(i, end = "")
print()


b.insert(4, 4)
print("Array after insertion:", end = "")
for i in (b):
    print(i, end = "")
print()

print("Acsess element is:", a[0])
print("acsess element is", b[2])




