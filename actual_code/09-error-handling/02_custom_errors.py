class InvalidUserChoiceError(Exception):
  pass


# class InvalidUserChoiceError extends Exception:

def get_valid_user_input():
  try:
    user_input = input("What's your favourite broadcasting network?")
    if user_input.lower() != "bbc":
      raise InvalidUserChoiceError("That's wrong - try again!")
    return user_input
  except InvalidUserChoiceError as error:
    print(error)
    return get_valid_user_input()

print(get_valid_user_input())