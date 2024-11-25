import numpy as np

np.b = False # type: ignore
a = np.full((4,4), np.b) # type: ignore
print(a)

print()
