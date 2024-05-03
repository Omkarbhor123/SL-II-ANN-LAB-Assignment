# Define the activation function
def activation_function(x,T):
    if x >= T:
        return 1
    else:
        return 0

# Define the AND NOT function
def ANDNOT(x1, x2):
    w1 = 1
    w2 = -1 
    Threshold = 1 # set the threshold value 

    net_input = w1*x1 + w2*x2 
    output = activation_function(net_input , Threshold)

    return output

# Test the AND NOT function
print("AND NOT Truth Table:")
print("X1  X2  Y")
print("--------------")
for x1 in [0, 1]:
    for x2 in [0, 1]:
        output = ANDNOT(x1, x2)
        print(f"{x1}   {x2}   {output}")
