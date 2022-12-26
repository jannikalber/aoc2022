import os
import random
file = open(f"Input\\{os.path.basename(__file__)[:-4]}.txt", "r")

print(f"Press the nice button! Here's a SNAFU number for you: {random.choice(file.readlines()).strip()}")
