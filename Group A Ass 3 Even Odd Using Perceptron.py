# Define step function
def step_function(x):
    if x >= 0:
        return 1
    else:
        return 0

# Define training data
training_data = [
    {'input': [1, 1, 0, 0, 0, 0], 'label': 1},  # 0 (odd)
    {'input': [1, 1, 0, 0, 0, 1], 'label': 0},  # 1 (even)
    {'input': [1, 1, 0, 0, 1, 0], 'label': 1},  # 2 (odd)
    {'input': [1, 1, 0, 1, 1, 1], 'label': 0},  # 3 (even)
    {'input': [1, 1, 0, 1, 0, 0], 'label': 1},  # 4 (odd)
    {'input': [1, 1, 0, 1, 0, 1], 'label': 0},  # 5 (even)
    {'input': [1, 1, 0, 1, 1, 0], 'label': 1},  # 6 (odd)
    {'input': [1, 1, 0, 1, 1, 1], 'label': 0},  # 7 (even)
    {'input': [1, 1, 1, 0, 0, 0], 'label': 1},  # 8 (odd)
    {'input': [1, 1, 1, 0, 0, 1], 'label': 0},  # 9 (even)
]

# Initialize weights
weights = [0, 0, 0, 0, 0, 1]

# Training the perceptron
for data in training_data:
    input_vector = data['input']
    label = data['label']
    output = step_function(sum(input_vector[i] * weights[i] for i in range(len(input_vector))))
    error = label - output
    weights = [weights[i] + input_vector[i] * error for i in range(len(weights))]

# Taking input from the user and predicting odd or even
j = int(input("Enter a Number (0-9): "))
input_vector = [int(x) for x in list('{0:06b}'.format(j))]
output = "odd" if step_function(sum(input_vector[i] * weights[i] for i in range(len(input_vector)))) == 0 else "even"
print(j, " is ", output)

