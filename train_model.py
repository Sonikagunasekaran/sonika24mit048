import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

# Dummy training data
X = np.array([
    [10, 20, 30],
    [2000, 3000, 4000],
    [15, 25, 35],
    [2500, 3500, 4500]
])

# Labels (0 = Normal, 1 = Attack)
y = np.array([0, 1, 0, 1])

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("Model trained and saved successfully!")