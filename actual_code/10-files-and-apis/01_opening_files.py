file = open("test.txt")

# <_io.TextIOWrapper name='test.txt' mode='r' encoding='UTF-8'>

# .read() -> open the whole file and make it available as a string
content = file.read()
print(content)
print(type(content))

file.seek(0)  # move the cursor to that byte
# .readlines() open the whole file and return a list of each line
contents = file.readlines()
print(contents) 

# for line in contents:
#   print(line.strip())

file.seek(0)
# .readline() -> line by line, generator function


line = file.readline()
print(line.strip())
print(file.tell())

while line:
  line = file.readline()
  print(line.strip(), file.tell())


file.close()

