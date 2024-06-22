import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target.reshape(-1, 1)

# One-hot encode the target labels
encoder = OneHotEncoder(sparse=False)
y = encoder.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the Feedforward Neural Network
model = Sequential([
    Dense(10, input_shape=(4,), activation='relu'),  # Input layer with 4 features and one hidden layer with 10 neurons
    Dense(10, activation='relu'),                   # Another hidden layer with 10 neurons
    Dense(3, activation='softmax')                  # Output layer with 3 neurons (one for each class) and softmax activation
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=5, verbose=1)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f'Test Accuracy: {accuracy:.4f}')

# Predicting a new sample
new_sample = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction = model.predict(new_sample)
predicted_class = np.argmax(prediction)
print(f'Predicted class for the new sample {new_sample}: {iris.target_names[predicted_class]}')
