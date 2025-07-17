import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
import time
import csv

class requester():

    def __init__(self, featuresRequesting):
        self.featuresRequesting = featuresRequesting

        # Setup the Open-Meteo API client with cache and retry on error
        cache_session = requests_cache.CachedSession('.cache', expire_after = 10000)
        retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
        self.openmeteo = openmeteo_requests.Client(session = retry_session)

        self.url = "https://historical-forecast-api.open-meteo.com/v1/forecast"
        self.count = 0

        self.file = open('Project_Coastle/trainingMeteoData.csv', 'a', newline='')
        self.writer = csv.writer(self.file)

        if self.file.tell() == 0:
            self.writer.writerow(self.featuresRequesting + ['label'])

        with open(self.file.name, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            row_count = sum(1 for row in csv_reader)-1  # Subtract 1 for header row

        self.getAlreadySolvedCities = row_count
        print(f"Already solved cities: {self.getAlreadySolvedCities}")

    def addToCSV(self, data,label):
        self.writer.writerow(data + [label])
        self.file.flush() 

    def getDatainList(self):
        return self.frame.to_numpy().tolist()

    def mean(dataPoints):
        return sum(dataPoints)/len(dataPoints)
    
    def getFromAPI(self,params, label):
        # print("sending request")
        
        responses = self.openmeteo.weather_api(self.url, params=params)
        response = responses[0]
        

        daily = response.Daily()

        daily_data = []
        for i, name in enumerate(self.featuresRequesting):
            values = daily.Variables(i).ValuesAsNumpy()
            # print(name)
            # If using a different metric instead of mean TODO

            daily_data.append(requester.mean(values))

        self.addToCSV(daily_data, label)
        print(daily_data)

        time.sleep(5.0)  # Sleep to avoid hitting rate limits
        self.count +=1
        print(self.count)




# Add entry
       
featureNames = ["temperature_2m_mean", "temperature_2m_max", "temperature_2m_min", "dew_point_2m_mean", "relative_humidity_2m_mean", "cloud_cover_mean", "apparent_temperature_mean", "cape_mean", "cape_max", "cape_min", "cloud_cover_max", "cloud_cover_min", "dew_point_2m_max", "dew_point_2m_min", "et0_fao_evapotranspiration_sum", "growing_degree_days_base_0_limit_50", "leaf_wetness_probability_mean", "precipitation_probability_mean", "precipitation_probability_min", "relative_humidity_2m_max", "relative_humidity_2m_min", "snowfall_water_equivalent_sum", "pressure_msl_mean", "pressure_msl_max", "pressure_msl_min", "surface_pressure_mean", "surface_pressure_max", "surface_pressure_min", "updraft_max", "visibility_mean", "visibility_min", "visibility_max", "winddirection_10m_dominant", "wind_gusts_10m_mean", "wind_speed_10m_mean", "wind_gusts_10m_min", "wind_speed_10m_min", "wet_bulb_temperature_2m_mean", "wet_bulb_temperature_2m_max", "wet_bulb_temperature_2m_min", "vapour_pressure_deficit_max", "soil_moisture_0_to_100cm_mean", "soil_moisture_0_to_10cm_mean", "soil_moisture_0_to_7cm_mean", "soil_moisture_28_to_100cm_mean", "soil_moisture_7_to_28cm_mean", "soil_temperature_0_to_100cm_mean", "soil_temperature_0_to_7cm_mean", "soil_temperature_28_to_100cm_mean", "soil_temperature_7_to_28cm_mean", "wind_speed_10m_max", "wind_gusts_10m_max", "wind_direction_10m_dominant", "shortwave_radiation_sum", "et0_fao_evapotranspiration", "precipitation_probability_max", "precipitation_hours", "precipitation_sum", "snowfall_sum", "showers_sum", "rain_sum", "daylight_duration", "sunshine_duration", "uv_index_max", "uv_index_clear_sky_max", "apparent_temperature_min", "apparent_temperature_max", "weather_code"]

print("requester created")
apiRequester = requester(featureNames)


params_base = {
    "daily": featureNames,
    "temperature_unit": "fahrenheit",
    "precipitation_unit": "inch"
}



print("extracting training data locations")
new_city_data = []
with open('Project_Coastle/trainingData_locations.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for i,row in enumerate(csv_reader):
        latitude = float(row['latitude'])
        longitude = float(row['longitude'])
        label = int(row['coastal'])
        name = str(row['name_of_city'])


        if i >= apiRequester.getAlreadySolvedCities:  # Skip already solved cities
            print(f"Adding city {name} with label {label}")
            new_city_data.append((latitude, longitude, label, name))


latitudes = [x[0] for x in new_city_data]
longitudes = [x[1] for x in new_city_data]
labels = [x[2] for x in new_city_data]
names = [x[3] for x in new_city_data]


print("getting weather data from API")
for i in range(len(latitudes)):
    single_params = {
        "latitude": latitudes[i],
        "longitude": longitudes[i],
        "start_date": "2025-01-01",
        "end_date": "2025-06-24",
        **params_base
    }

    apiRequester.getFromAPI(single_params, labels[i])
    print(f"Processed city name: {names[i]}, label: {labels[i]}, latitude: {latitudes[i]}, longitude: {longitudes[i]}")

apiRequester.file.close()
print("Finished writing to CSV")