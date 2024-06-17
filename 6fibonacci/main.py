print("""**********************

fibonacci sayı serisi
""")

a = 1
b = 1

fibonacci = [a,b]

for i in range(100):
    a,b = b,a+b

    fibonacci.append(b)
print(fibonacci)