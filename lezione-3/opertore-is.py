a = [1,2,3]
b = [1,2,3]

a[1] = 13

print(a == b)
print(a is b)

print(id(a))
print(id(b))

c = a

print(id(c))
print(a is c)

x = "ciao"
y = "ciao"

print(x == y)
print(x is y)

print(id(x))
print(id(y))