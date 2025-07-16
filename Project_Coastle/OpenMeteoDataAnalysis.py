import numpy as np
import pandas as pd
from scipy.stats import pointbiserialr, linregress
from matplotlib import pyplot as plt

df = pd.read_csv('Project_Coastle/trainingMeteoData.csv')

labels = pd.read_csv('Project_Coastle/trainingData_LabeledLocations.csv')['coastal'].to_numpy()
labels = labels[:len(df)]

thresholdNan = 50.0

total_rows = len(df)
nan_counts = df.isna().sum()


for feature, count in nan_counts.items():
    if count > 0:
        percent = 100 * count / total_rows
        print(f"{feature}: {count} NaNs ({percent:.2f}%)")

        #eliminate variabels above threshold
        if percent > thresholdNan:
            print(f"Dropping {feature} due to NaN percentage: {percent:.2f}%")
            df.drop(columns=[feature], inplace=True)
        elif df[feature].nunique() <= 1:
            print(f"Dropping {feature} due to constant value")
            df.drop(columns=[feature], inplace=True)


biserialCorrelations = []    
linearRegressCorrelations = []    

for feature in df.columns:
    # Calculate correlations with this feature
    if not df[feature].isna().any():
        bisereialCorr, p = pointbiserialr(df[feature], labels)
        biserialCorrelations.append((bisereialCorr,feature))
        print(f"Point Biserial Correlation between {feature} and label: {bisereialCorr:.2f}")
    else:
        biserialCorrelations.append((0.0, feature))

    linregress_result = linregress(df[feature], labels)
    linearRegressCorrelations.append((linregress_result.rvalue, feature))
    print(f"Linear Regression between {feature} and label: r-value={linregress_result.rvalue:.2f}")


#plot a bar chart of correlations side by side (Linear Regression bar -> blue, Point Biserial bar -> orange)
plt.figure(figsize=(15, 8))
biserial_corrs = [x[0] for x in biserialCorrelations]
linear_regress_corrs = [x[0] for x in linearRegressCorrelations]
features = [x[1] for x in linearRegressCorrelations]

bar_width = 0.5
x = range(len(features))

plt.bar(x, biserial_corrs, width=bar_width, label='Point Biserial', color='orange')
plt.bar([i + bar_width for i in x], linear_regress_corrs, width=bar_width, label='Linear Regression', color='blue')

plt.xlabel('Features')
plt.ylabel('Correlation Coefficient')
plt.title('Feature Correlations with Label')
plt.xticks([i + bar_width / 2 for i in x], features, rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


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


