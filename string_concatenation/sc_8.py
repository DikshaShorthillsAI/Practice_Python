# Inefficient method using '+'
result = ""
for i in range(1000):
    result += str(i)

# Efficient method using 'join()'
result = " ".join(str(i) for i in range(1000))
print(result)