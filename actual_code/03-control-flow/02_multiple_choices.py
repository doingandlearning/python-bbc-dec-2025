user_channel = input("What channel would you like to watch? ").lower().strip()

if user_channel == "bbc1" or user_channel == "bbc2":
  print("Traitors or University Challenge!")
elif user_channel == "cbeebies":
  print("Time for Bluey!")
elif user_channel.startswith("sky") and user_channel.find("news") > 0:
  print("BBC News is better.")
elif not user_channel.startswith("bbc"):
  print("Are you sure that's a BBC channel?")
else: 
  print("I don't know that channel")


match user_channel:
  case "bbc1":
    print("Traitors")
  case "bbc2":
    print("University Challenge")
  case "cbeebies":
    print("Bluey")
  case _:
    print("Don't know that one.")