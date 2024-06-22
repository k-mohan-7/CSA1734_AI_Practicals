import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Sample data
# Features: [Height (cm), Weight (kg), Shoe Size (cm)]
X = np.array([
    [170, 65, 40],
    [180, 80, 42],
    [160, 50, 38],
    [175, 75, 41],
    [185, 90, 44],
    [155, 48, 37],
    [165, 55, 39],
    [190, 85, 43]
])

# Labels: 0 for 'Male', 1 for 'Female'
y = np.array([0, 0, 1, 0, 0, 1, 1, 0])

# Create Decision Tree Classifier
clf = DecisionTreeClassifier()

# Train the classifier
clf.fit(X, y)

# Predicting a new sample
new_sample = np.array([[165, 60, 39]])  # Should be 'Female' (1)
prediction = clf.predict(new_sample)
print(f"Prediction for the new sample {new_sample}: {'Female' if prediction[0] == 1 else 'Male'}")

# Visualizing the Decision Tree
plt.figure(figsize=(12,8))
tree.plot_tree(clf, feature_names=["Height", "Weight", "Shoe Size"], class_names=["Male", "Female"], filled=True)
plt.show()
