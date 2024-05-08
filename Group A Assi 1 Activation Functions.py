import numpy as np
import matplotlib.pyplot as plt

# Define activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))


# Define input range
x = np.linspace(-5, 5, 100)

# Plot activation functions
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(x, sigmoid(x), label='Sigmoid')
plt.title('Sigmoid Activation')
plt.legend()

plt.subplot(2, 3, 2)
plt.plot(x, tanh(x), label='Tanh')
plt.title('Tanh Activation')
plt.legend()

plt.subplot(2, 3, 3)
plt.plot(x, relu(x), label='ReLU')
plt.title('ReLU Activation')
plt.legend()

plt.subplot(2, 3, 5)
plt.plot(x, softmax(x), label='Softmax')
plt.title('Softmax Activation')
plt.legend()

plt.tight_layout()
plt.show()
