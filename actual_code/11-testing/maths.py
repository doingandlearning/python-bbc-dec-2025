def add(a: int | float, b: int | float):
  if not isinstance(a, (int,float)) or not isinstance(b, (int,float)):
    raise TypeError("Both arguments must be numbers.")
  
  if isinstance(a, bool) or isinstance(b, bool):
    raise TypeError("Both arguments must be numbers.") 

  return a + b


"""
- Pattern for writing
- Happy path
- Edge cases 
- Parametrisation
- Unhappy paths - exception testing
---
- Mocking 
- Integration tests/E2E

"""