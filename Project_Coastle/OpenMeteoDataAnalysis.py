import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv('Project_Coastle/trainingMeteoData.csv')
label_Series = df['label']
df.drop(columns=['label'], inplace=True)

# ['growing_degree_days_base_0_limit_50', 'leaf_wetness_probability_mean', 'updraft_max', 'soil_moisture_0_to_100cm_mean', 'soil_moisture_0_to_7cm_mean', 'soil_moisture_28_to_100cm_mean', 'soil_moisture_7_to_28cm_mean', 'soil_temperature_0_to_100cm_mean', 'soil_temperature_0_to_7cm_mean', 'soil_temperature_28_to_100cm_mean', 'soil_temperature_7_to_28cm_mean']


thresholdNan = 50.0

total_rows = len(df)
nan_counts = df.isna().sum()

droppedFeatures = []
linearRegression = []

for feature, count in nan_counts.items():
    if count > 0:
        percent = 100 * count / total_rows
        print(f"{feature}: {count} NaNs ({percent:.2f}%)")

        #eliminate variabels above threshold
        if percent > thresholdNan:
            print(f"Dropping {feature} due to NaN percentage: {percent:.2f}%")
            df.drop(columns=[feature], inplace=True)
            droppedFeatures.append(feature)
        elif df[feature].nunique() <= 1:
            print(f"Dropping {feature} due to constant value")
            df.drop(columns=[feature], inplace=True)
            droppedFeatures.append(feature)



def findbestPolynomialDegree(x, y, max_degree=10):
    best_degree = 1
    best_r2 = float('-inf')

    for degree in range(1, max_degree + 1):
        poly_features = PolynomialFeatures(degree=degree, include_bias=False)
        X_poly = poly_features.fit_transform(x.reshape(-1, 1))
        model = LinearRegression()
        model.fit(X_poly, y)
        y_pred = model.predict(X_poly)
        r2 = r2_score(y, y_pred)

        if r2 > best_r2:
            best_r2 = r2
            best_degree = degree

        if degree == 1:
            linearRegression.append(r2)
            print(f"Linear Regression between feature and label: r-squared={r2:.2f}")
    return best_degree, best_r2



biserialCorrelations = []    
polyRegressCorrelations = []    

for feature in df.columns:

    df[feature].fillna(df[feature].mean(), inplace=True)

    # Polynomial Regression correlation
    best_degree, best_r2 = findbestPolynomialDegree(df[feature].values, label_Series.values)

    polyRegressCorrelations.append((best_r2, feature))
    # print(f"Polynomial Regression between {feature} and label: r-squared={best_r2:.2f}")


    if abs(best_r2) < 0.25 :
        droppedFeatures.append(feature)


#plot a bar chart of correlations side by side (Linear Regression bar -> blue, Point Biserial bar -> orange)
plt.figure(figsize=(15, 8))
poly_regress_corrs = [x[0] for x in polyRegressCorrelations]
features = [x[1] for x in polyRegressCorrelations]

bar_width = 0.5
x = range(len(features))
print(linearRegression)

plt.bar([i for i in x], poly_regress_corrs, width=bar_width, label='Polynomial Regression', color='blue')
plt.bar([i for i in x], linearRegression, width=bar_width, label='Linear Regression', color='red')

plt.xlabel('Features')
plt.ylabel('Correlation Coefficient')
plt.title('Feature Correlations with Label')
plt.legend()
plt.tight_layout()
plt.show()

print(droppedFeatures)


# def filter_features_by_nan_and_corr(df, corr_series, nan_threshold=0.5, corr_threshold=0.08):
#         total_rows = len(df)
#         nan_counts = df.isna().sum()

#         selected_features = []
#         for feature in df.columns:
#             nan_frac = nan_counts[feature] / total_rows
#             corr_val = corr_series.get(feature, 0)

#             if nan_frac <= nan_threshold and abs(corr_val) >= corr_threshold:
#                 selected_features.append(feature)
#             else:
#                 print(f"Dropping {feature}: NaNs {nan_frac:.2%}, Corr {corr_val:.3f}")

#         filtered_df = df[selected_features].copy()

#         print(filtered_df.columns)
#         return filtered_df, selected_features



    # def getListDataset(self):
    #     nan_counts = self.frame.isna().sum()
    #     total_rows = len(self.frame)

    #     for feature, count in nan_counts.items():
    #         if count > 0:
    #             percent = 100 * count / total_rows
    #             print(f"{feature}: {count} NaNs ({percent:.2f}%)")


    #     # CSV
    #     labelsFromCSV = []
    #     with open('CityProject/trainingData.csv', 'r') as file:
    #         csv_reader = csv.DictReader(file)
    #         for row in csv_reader:
    #             coastal = float(row['coastal'])
    #             labelsFromCSV.append(coastal)

    #     labels= pd.Series(labelsFromCSV)
    #     print(labels.head(20))

    #     self.frame["label"] = labels

    #     correlations = self.frame.corr()['label'].drop('label')
    #     filtered_df, kept_features = requester.filter_features_by_nan_and_corr(self.frame, correlations)

    #     filtered_df["label"] = labels

    #     # print(self.frame.head()) 
    #     data = [
    #         (row[:-1].tolist(), row[-1])
    #         for row in filtered_df.to_numpy()
    #     ]
        
    #     # for row in self.frame.to_numpy():
    #     #     print(row[-1])
    #     #     print(row[-2])

    #     return data


