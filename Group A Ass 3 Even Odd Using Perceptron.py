import numpy as np

# Define the Perceptron class
class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand()
        self.learning_rate = learning_rate

    def activation_function(self, x):
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        weighted_sum = np.dot(inputs, self.weights) + self.bias
        return self.activation_function(weighted_sum)

    def train(self, input_vectors, labels):
        for input_vec, label in zip(input_vectors, labels):
            prediction = self.predict(input_vec)
            error = label - prediction
            self.weights += self.learning_rate * error * input_vec
            self.bias += self.learning_rate * error

# Convert ASCII digits to binary vectors
def ascii_to_binary(char):
    binary = np.array([int(bit) for bit in format(ord(char), '08b')])
    return binary

# Training data
input_vectors = [ascii_to_binary(str(i)) for i in range(10)]
labels = [0 if i % 2 == 0 else 1 for i in range(10)]

# Create the Perceptron
perceptron = Perceptron(input_size=8, learning_rate=0.1)

# Train the Perceptron
epochs = 10
for epoch in range(epochs):
    perceptron.train(input_vectors, labels)

# Test the Perceptron
print("ASCII Digit | Even/Odd")
print("------------|---------")
for digit in range(10):
    input_vec = ascii_to_binary(str(digit))
    prediction = perceptron.predict(input_vec)
    print(f"     {digit}     | {'Even' if prediction == 0 else 'Odd'}")
