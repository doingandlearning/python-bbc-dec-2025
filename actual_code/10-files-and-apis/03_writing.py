with open("log.txt", mode="w") as file:
  file.write("Hello!\n")
  file.write("Python is great\n")
  file.write("Almost there :) \n")

# Cmd-/  Ctrl-/

with open("log.txt", mode="a") as file:
  file.write("This is another line\n")
  file.write("This is yet another line\n")