import numpy as np

# Define the weights and bias
weights = np.array([[-1, -1], [1, 1]])
bias = 1

# Define the activation function
def activation_function(x):
    if x >= 0:
        return 1
    else:
        return 0

# Define the ANDNOT function
def andnot(x1, x2):
    z = np.dot(weights, [x1, x2]) + bias
    y = activation_function(z)
    return y

# Test the ANDNOT function
print("ANDNOT Truth Table:")
print("x1 x2 | y")
print("----------")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        y = andnot(x1, x2)
        print(f"{x1}   {x2} | {y}")
