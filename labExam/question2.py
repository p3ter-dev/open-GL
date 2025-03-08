import numpy as np
def compute_cross_product(arrayx, arrayy):
    return np.cross(arrayx, arrayy)

arrayx = [1, 2, 3]
arrayy = [4, 5, 6]
result = compute_cross_product(arrayx, arrayy)
print(result)
