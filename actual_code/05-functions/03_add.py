def add(a, b, c=0, d=0):
  return a + b + c + d

print(add(1,2))
print(add(1,2,3))
print(add(1,2,3,4))

def add(*numbers):  # *args
  total = 0
  for n in numbers:
    total = total + n
  return total 

print(add(1,2))
print(add(1,2,3))
print(add(1,2,3,4))
print(add(1,2,3,4,5))
print(add(1,2,3,4,5,6))
print(add(1,2,3,4,5,6,7))
print(add(1,2,3,4,5,6,7,8))