from Project_Coastle.Artificial_Location import produceCoordinates
from Project_Coastle.OpenMeteoDataExtraction import requester
from Project_Coastle.LinearClassificationMethods import linearClassifyingTools

theta = [723431.4337753518, 712993.8948366022, 749109.4483124813, 764820.2717569014, 955592.0511495954, 580372.8867605128, 761092.6247744949, 6898602.283585012, 4217928.857144054, 1153752.3657144473, 114760.38285708115, 806577.2255757088, 724114.3523169429, 978.8817717904594, -12509.135285250066, 982364.2400000235, 835840.6400000827, 10.404836243887045, 9968757.672373189, 9971765.330199325, 11449396.055961814, 11453983.958572134, 11436361.64465394, -1187116.9158289148, 1253128.1479566807, 35167.72581479902, 2036661.3403538628, 174724.15303197457, 154558.86808467927, 70342.06218089082, 736430.3954856123, 754502.108145347, 728379.8299943341, -5041.1412814612295, 2376.1148061318313, 294410.81321828964, 295778.0834915718, 2036661.3403538628, 978.8817717904594, -17644.13142856818, -5378.3942857156635, 72.83381693574349, 0.0, 346.6071572496816, 776445.7529467562, 784559.4045078588, 312169.2571428689]
theta_zero =  9779.0
# theta = [8.643258601597381, 12.101914978027345, 11.659049846104217, 6.169523402622758, 2.870952322674647, 11.618930696759904, 596.4833307979787, 316.0, 11.714285714285722, 0.5371428571428569, 10.374570922851568, 13.266375950404573, 0.007278539586280053, 0.022857142857142854, -2.519999999999996, 17.268571428571427, -0.013714773995502583, 6.95962960379461, 6.482071358816938, 7.61528424944197, -19222.518794642856, 7647.169185267856, -57791.5264732143, 2.862043854849679, 5.395885495798929, 2.305270860365459, 9.666959849766329, 8.520303410121372, 11.15753283909389, -0.4202386857782092, 0.6171424865722663, 0.007278539586280053, -0.029741278955979007, 0.0, -0.027019118749137434, 14.507941207885736, 8.499383490426197, 1.7542857142857144]
# theta_zero =  0.0

# theta = [8.643258601597381, 12.101914978027345, 11.659049846104217, 6.169523402622758, 2.870952322674647, 11.618930696759904, 596.4833307979787, 316.0, 11.714285714285722, 0.5371428571428569, 10.374570922851568, 13.266375950404573, 0.007278539586280053, 0.022857142857142854, -2.519999999999996, 17.268571428571427, -0.013714773995502583, 6.95962960379461, 6.482071358816938, 7.61528424944197, -19222.518794642856, 7647.169185267856, -57791.5264732143, 2.305270860365459, 9.666959849766329, 8.520303410121372, 11.15753283909389, -0.4202386857782092, 0.6171424865722663, 0.007278539586280053, -0.029741278955979007, -0.027019118749137434, 14.507941207885736, 1.7542857142857144]
# theta_zero =  0.0


print("gemini called")
coordinates = [
    (43.66,-70.26,1),
(35.21,-101.83,-1),
(30.33,-81.66,1),
(31.76,-106.49,-1),
(30.27,-97.74,-1),
(35.60,-82.55,-1),
(32.78,-79.93,1),
(32.08,-81.09,1),
(30.33,-81.66,1),
(27.95,-82.46,1),
(36.85,-76.29,1),
(39.29,-76.61,1),
(39.36,-74.42,1)
]

# coordinates = []
# for i in range(10):
#     if i%2 ==0:
#         coordinates.append(produceCoordinates("not coastal at all."))
#     else:
#         coordinates.append(produceCoordinates("right near the coast."))


print(coordinates)

request = requester()

# featureNames =['temperature_2m_mean', 'temperature_2m_min', 'dew_point_2m_mean',
#       'relative_humidity_2m_mean', 'cloud_cover_mean',
#       'apparent_temperature_mean', 'cape_mean', 'cape_min', 'cloud_cover_max',
#       'cloud_cover_min', 'dew_point_2m_max', 'dew_point_2m_min',
#       'et0_fao_evapotranspiration_sum', 'precipitation_probability_min',
#       'relative_humidity_2m_max', 'relative_humidity_2m_min',
#       'pressure_msl_min', 'surface_pressure_mean', 'surface_pressure_max',
#       'surface_pressure_min', 'visibility_mean', 'visibility_min',
#       'visibility_max', 'wind_speed_10m_min', 'wet_bulb_temperature_2m_mean',
#       'wet_bulb_temperature_2m_max', 'wet_bulb_temperature_2m_min',
#       'vapour_pressure_deficit_max', 'wind_gusts_10m_max',
#       'et0_fao_evapotranspiration', 'precipitation_sum', 'rain_sum',
#       'apparent_temperature_min', 'weather_code']


# featureNames = ['temperature_2m_mean', 'temperature_2m_min', 'dew_point_2m_mean',
#        'relative_humidity_2m_mean', 'cloud_cover_mean',
#        'apparent_temperature_mean', 'cape_mean', 'cape_min', 'cloud_cover_max',
#        'cloud_cover_min', 'dew_point_2m_max', 'dew_point_2m_min',
#        'et0_fao_evapotranspiration_sum', 'precipitation_probability_min',
#        'relative_humidity_2m_max', 'relative_humidity_2m_min',
#        'pressure_msl_min', 'surface_pressure_mean', 'surface_pressure_max',
#        'surface_pressure_min', 'visibility_mean', 'visibility_min',
#        'visibility_max', 'wind_speed_10m_mean', 'wind_gusts_10m_min',
#        'wind_speed_10m_min', 'wet_bulb_temperature_2m_mean',
#        'wet_bulb_temperature_2m_max', 'wet_bulb_temperature_2m_min',
#        'vapour_pressure_deficit_max', 'wind_gusts_10m_max',
#        'et0_fao_evapotranspiration', 'precipitation_sum', 'showers_sum',
#        'rain_sum', 'apparent_temperature_min', 'apparent_temperature_max',
#        'weather_code']

featureNames =['temperature_2m_mean', 'temperature_2m_max', 'temperature_2m_min',
       'dew_point_2m_mean', 'relative_humidity_2m_mean', 'cloud_cover_mean',
       'apparent_temperature_mean', 'cape_mean', 'cape_min', 'cloud_cover_max',
       'cloud_cover_min', 'dew_point_2m_max', 'dew_point_2m_min',
       'et0_fao_evapotranspiration_sum', 'precipitation_probability_mean',
       'relative_humidity_2m_max', 'relative_humidity_2m_min',
       'snowfall_water_equivalent_sum', 'pressure_msl_max', 'pressure_msl_min',
       'surface_pressure_mean', 'surface_pressure_max', 'surface_pressure_min',
       'visibility_mean', 'visibility_min', 'visibility_max',
       'winddirection_10m_dominant', 'wind_speed_10m_mean',
       'wind_gusts_10m_min', 'wind_speed_10m_min',
       'wet_bulb_temperature_2m_mean', 'wet_bulb_temperature_2m_max',
       'wet_bulb_temperature_2m_min', 'vapour_pressure_deficit_max',
       'soil_moisture_0_to_10cm_mean', 'wind_speed_10m_max',
       'wind_gusts_10m_max', 'wind_direction_10m_dominant',
       'et0_fao_evapotranspiration', 'precipitation_probability_max',
       'precipitation_hours', 'snowfall_sum', 'showers_sum', 'rain_sum',
       'apparent_temperature_min', 'apparent_temperature_max', 'weather_code']

params_base = {
    "daily": featureNames,
    "temperature_unit": "fahrenheit",
    "precipitation_unit": "inch"
}

request.reset()

latitudes = [x[0] for x in coordinates]
longitudes = [x[1] for x in coordinates]

for i in range(len(latitudes)):

    print(latitudes[i],longitudes[i])

    single_params = {
        "latitude": latitudes[i],
        "longitude": longitudes[i],
        "start_date": "2025-01-01",
        "end_date": "2025-06-24",
        **params_base
    }

    request.getFromAPI(single_params,featureNames)

    data = request.getDatainList()[-1]
    print(len(data))
    print(len(theta))
    # print(data)
    value = linearClassifyingTools.sign(linearClassifyingTools.dot(theta,data) + theta_zero)
    if value == 1:
        print("Guess is Coastal")
    else:
        print("Guess is Not Coastal")


    if coordinates[i][2] == 1:
        print("Real location is Coastal")
    else:
        print("Real location is Not Coastal")

    request.reset()

