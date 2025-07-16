import pandas as pd
from sklearn.model_selection import train_test_split
from sympy import per
from LinearClassifier import Perceptron
import numpy as np

df = pd.read_csv('Project_Coastle/trainingMeteoData.csv').replace(np.nan, 0)
label_df = pd.read_csv('Project_Coastle/trainingData_LabeledLocations.csv')

# Create a new DataFrame with two columns: 'features' and 'label'
combined_df = pd.DataFrame({
    'features': df.values.tolist(),
    'label': label_df['coastal'].values
})


# Convert to numpy array for further processing if needed
data = combined_df[['features', 'label']].to_numpy()

# train_test_split
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
print(train_data[0])

perceptron = Perceptron(num_features= len(train_data[0][0]))

perceptron.fit(train_data, tauRuns=100)
print("Training complete")

perceptron.plotConvergence(dataSpread=5)
print("Convergence plot shown")


correct = 0
for i, test_point in enumerate(test_data):
    
    prediction = perceptron.predict(test_point[:-1][0])
    actual = test_point[-1]

    if prediction == actual:
        correct+=1

    print(f"Location {label_df.iloc[i+1]['name_of_city']}: Predicted={prediction}, Actual={actual}, {'Correct' if prediction == actual else 'Incorrect'}")

accuracy = correct / len(test_data) * 100 
print(f"Accuracy on test set: {accuracy:.2f}%")