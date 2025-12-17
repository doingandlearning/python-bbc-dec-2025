class Shape:
  def __init__(self, type):
    self.type = type

_triangle = Shape("triangle")

if __name__ == "__main__":  
  print("Hello from utils.py!!")
  print(f"utils.py __name__ is {__name__}")