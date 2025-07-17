import pandas as pd
from sklearn.model_selection import train_test_split
from sympy import per
from LinearClassifier import Perceptron
import numpy as np

df = pd.read_csv('Project_Coastle/trainingMeteoData.csv').replace(np.nan, 0)
label_Series = df['label']

unsignificantFeatures = ['growing_degree_days_base_0_limit_50', 'leaf_wetness_probability_mean', 'updraft_max', 'soil_moisture_0_to_100cm_mean', 'soil_moisture_0_to_7cm_mean', 'soil_moisture_28_to_100cm_mean', 'soil_moisture_7_to_28cm_mean', 'soil_temperature_0_to_100cm_mean', 'soil_temperature_0_to_7cm_mean', 'soil_temperature_28_to_100cm_mean', 'soil_temperature_7_to_28cm_mean', 'temperature_2m_mean', 'temperature_2m_max', 'apparent_temperature_mean', 'cape_mean', 'cape_max', 'cape_min', 'et0_fao_evapotranspiration_sum', 'precipitation_probability_min', 'snowfall_water_equivalent_sum', 'pressure_msl_mean', 'pressure_msl_max', 'winddirection_10m_dominant', 'wind_gusts_10m_mean', 'wind_speed_10m_mean', 'wind_gusts_10m_min', 'wind_speed_10m_min', 'wet_bulb_temperature_2m_max', 'soil_moisture_0_to_10cm_mean', 'wind_speed_10m_max', 'wind_gusts_10m_max', 'wind_direction_10m_dominant', 'shortwave_radiation_sum', 'et0_fao_evapotranspiration', 'precipitation_hours', 'precipitation_sum', 'snowfall_sum', 'showers_sum', 'rain_sum', 'daylight_duration', 'sunshine_duration', 'uv_index_max', 'uv_index_clear_sky_max', 'apparent_temperature_max']
df.drop(columns=unsignificantFeatures, inplace=True)

# Create a new DataFrame with two columns: 'features' and 'label'
combined_df = pd.DataFrame({
    'features': df.values.tolist(),
    'label': label_Series.values
})

# Convert to numpy array for further processing if needed
data = combined_df[['features', 'label']].to_numpy()

# train_test_split
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
# print(train_data[0])

perceptron = Perceptron(num_features= len(train_data[0][0]))

perceptron.fit(train_data, tauRuns=1000)
print("Training complete")

perceptron.plotConvergence(dataSpread=5)
print("Convergence plot shown")


correct = 0
for i, test_point in enumerate(test_data):
    
    prediction = perceptron.predict(test_point[:-1][0])
    actual = test_point[-1]

    if prediction == actual:
        correct+=1

    print(f"Location {label_Series[i+1]}: Predicted={prediction}, Actual={actual}, {'Correct' if prediction == actual else 'Incorrect'}")

accuracy = correct / len(test_data) * 100 
print(f"Accuracy on test set: {accuracy:.2f}%")