import random
import os

import utils as u # namespaced! aliasing/rename the libraries locally
import util.arithmetic 

import sys

print(sys.path)
# sys.path.append()

print(util.arithmetic)
# import numpy as np
# import pandas as pd

print("Hello!")
print(random.choice(["Heads", "Tails"]))
print(os.cpu_count())


print(__name__)
print(__file__)
print(dir(u))

# __main__.User