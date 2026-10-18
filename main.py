# Welcome to Python Compiler! Press Ctrl+Enter to run
print("Hello, World!")

# Pandas example
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print("\nDataFrame:\n", df)

# Matplotlib example (uncomment to run)
# import matplotlib.pyplot as plt
# plt.plot([1, 2, 3], [1, 4, 9])
# plt.title('Simple Plot')
# plt.show()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

person = Person("Alice", 30)
print(person.greet())

print("Hello, World!")

print("Hello, World!")

for i in range(10):
    print(i)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(f"Array: {arr}")
print(f"Mean: {np.mean(arr)}")
print(f"Sum: {np.sum(arr)}")