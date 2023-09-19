t = (1, 2, 3)

print(t)

x = 0.125
print(x.as_integer_ratio())

numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)

a = 1
b = 0
a, b = b, a
print(a, b)