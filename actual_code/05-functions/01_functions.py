def print_message_with_seperator(message, seperator="*", degrees_of_separation=10):
  """
  A function that print hello.
  """
  print(seperator * degrees_of_separation)
  print(message)
  print(seperator * degrees_of_separation)

print_message_with_seperator("Hello from Manchester!")
print_message_with_seperator("Hello from Salford!", "=*=")
print_message_with_seperator("Hello from London!", "@-@", 7)
print_message_with_seperator("Hello from Belfast", degrees_of_separation=20)
print_message_with_seperator(
  degrees_of_separation=8, 
  seperator="%", 
  message="Hello from Space!"
  )




