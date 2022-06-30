import pandas as pd
from sklearn.impute import SimpleImputer

Dataset_URL = "https://raw.githubusercontent.com/cognizance-amrita/AI-Tasks/main/Task-1/Q2-Dataset.csv?raw=true"
df = pd.read_csv(Dataset_URL, index_col=0)

print("The perentage of NaN values in columns with NaN values:")
print(df[df.columns[df.isnull().any()]].isnull().sum() * 100 / df.shape[0])

print("\nThe 'Alley' column has too many NaN values so such columns would be inefficient for the model to train on.")
print("After dropping 'Alley' column, the percentage of NaN values in columns with NaN values:")
# The 'Alley' column has a lot of null values. So we need to drop it.
df.drop(['Alley'], axis=1, inplace=True)
print(df[df.columns[df.isnull().any()]].isnull().sum() * 100 / df.shape[0])

temp_cols = df.columns

# IMPUTING THE DATA-FRAME BY FILLING MOST FREQUENT ENTRIES IN-PLACE OF NaN ENTRIES.

# Model Creation
imputer = SimpleImputer(strategy='most_frequent')

# fitting the imputer on the original dataset
imputer.fit(df)

# Imputing the missing values in train, validation and test inputs
df = imputer.transform(df)

# Model Creation
imputer = SimpleImputer(strategy='most_frequent')

# fitting the imputer on the original dataset
imputer.fit(df)

# Imputing the missing values in train, validation and test inputs
df = imputer.transform(df)

df = pd.DataFrame(df, columns=temp_cols)  # Converting the NumpY array to Pandas DataFrame

print("\nChecking if any NaN entry is left in any column: ")
print(df.isnull().any())