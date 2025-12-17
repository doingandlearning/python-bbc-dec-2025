import traceback

def get_number_from_user():
  try:
    user_number = int(input("Give me a number: "))
    return user_number
  except ValueError as e:
    # log for sysop -> slack message
    tb = traceback.format_exc()
    print(tb)

    print("You didn't give me a number - try again.")
    return get_number_from_user()
  except ArithmeticError:
    print("Some unknown maths tried to happen")

  


# files, databases, network, users, ... 

try:
  user_input = get_number_from_user()  # raise ValueError("invalid literal for int() with base 10: 'one'")
except SyntaxError:
  print("Invalid Syntax")
except Exception as e:
  tb = traceback.format_exc()
  print(tb)
  print("Something unexpected happen. Come back later.")
else:
  print("From the else block:")
  print(user_input + 1) 
finally:
  print("This will always run!")



print("Program keeps running!")