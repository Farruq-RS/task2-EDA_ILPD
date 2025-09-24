import pandas as pd # data manipulation
import numpy as np # numerical computations
import matplotlib.pyplot as plt # data visualization
import seaborn as sns # statistical data visualization

#Load data
df = pd.read_csv('indian_liver_patient.csv') 
print(df.head()) # Display first few rows
print(df.info()) # Display data types, columns and non-null values
print(df.describe()) # Display summary statistics

#Data cleaning
#Missing values
print("Missing values before:", df.isnull().sum()) # Check for missing values
# Fill missing values in 'Albumin_and_Globulin_Ratio' with median
median_ratio = df['Albumin_and_Globulin_Ratio'].median() # Calculate median
df['Albumin_and_Globulin_Ratio'] = df['Albumin_and_Globulin_Ratio'].fillna(median_ratio) # Fill missing values
print("Missing values after:", df.isnull().sum()) # Verify no missing values remain

#Gender mapping
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0}) # Convert from categorical to numerical

#Basic feaure engineering
#To understand whether children or elderly patients are more prone to liver issues
df['Is_Child'] = (df['Age'] < 18).astype(int) # Children under 18
df['Is_Senior'] = (df['Age'] > 60).astype(int) # Seniors over 60
print(df[['Age', 'Is_Child', 'Is_Senior']].head()) # Verify new columns


#Data visualization
numeric_cols = ['Age', 'Total_Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase',
                'Alamine_Aminotransferase', 'Aspartate_Aminotransferase',
                'Total_Protiens', 'Albumin', 'Albumin_and_Globulin_Ratio']

# Histograms - Shows how values are spread out
for col in numeric_cols:
    plt.figure(figsize=(6,4)) # Set figure size
    sns.histplot(df[col], kde=True) # Plot histogram with KDE 
    plt.title(f'Histogram of {col}') 
    plt.show() # Display plot

# Boxplots - Shows quartiles, median, and outliers, helps detect strange or extreme values
for col in numeric_cols:
    plt.figure(figsize=(6,4)) # Set figure size
    sns.boxplot(y=df[col]) # Plot boxplot
    plt.title(f'Boxplot of {col}') 
    plt.show() # Display plot

# Pairplot 
sns.pairplot(df[numeric_cols + ['Dataset']], hue='Dataset') # 'Dataset' is the target variable
plt.show() # Shows feature relationships, color-coded by disease

# Correlation heatmap
corr = df[numeric_cols].corr() # Compute correlation matrix
plt.figure(figsize=(10,8)) # Set figure size
sns.heatmap(corr, annot=True, cmap='coolwarm') # Plot heatmap with annotations
plt.title('Correlation Matrix') 
plt.show() # Displays correlations between features

df.to_csv('cleaned_ilpd.csv', index=False)
