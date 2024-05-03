# Define the activation function
def activation_function(x):
    if x >= 0:
        return 1
    else:
        return 0

# Define the ANDNOT function
def ANDNOT(x1, x2):
    w1 = 1
    w2 = 1
    w3 = -1
    b = -1.5

    net_input = w1*x1 + w2*x2 + b
    output = activation_function(net_input)

    return output

# Test the ANDNOT function
print("ANDNOT Truth Table:")
print("x1 x2 | Output")
print("---------------")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        output = ANDNOT(x1, x2)
        print(f"{x1}   {x2} | {output}")
