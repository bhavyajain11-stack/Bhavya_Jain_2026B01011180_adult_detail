
# ==========================================
# ADULT INCOME PREDICTION
# COMPLETE DATA CLEANING
# Using Only Pandas and NumPy
# ==========================================

# STEP 1: Import Libraries

import pandas as pd
import numpy as np


# STEP 2: Load Dataset

df = pd.read_csv("Adult Data.csv", header=None)

print("Original Dataset:")
print(df.head())


# STEP 3: Add Column Names

columns = [
    "age",
    "workclass",
    "fnlwgt",
    "education",
    "education_num",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "capital_gain",
    "capital_loss",
    "hours_per_week",
    "native_country",
    "income"
]

df.columns = columns

print("\nColumn Names:")
print(df.columns)


# STEP 4: Check Dataset Information

print("\nDataset Information:")
print(df.info())


# STEP 5: Check Dataset Shape

print("\nDataset Shape:")
print(df.shape)


# STEP 6: Remove Extra Spaces

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

print("\nExtra Spaces Removed")


# STEP 7: Replace '?' with NaN

df.replace("?", np.nan, inplace=True)

print("\nMissing Values:")
print(df.isnull().sum())


# STEP 8: Check Duplicate Values

print("\nDuplicate Rows:")
print(df.duplicated().sum())


# STEP 9: Remove Duplicate Rows

df.drop_duplicates(inplace=True)

print("\nDuplicates Removed")


# STEP 10: Convert Numeric Columns

numeric_columns = [
    "age",
    "fnlwgt",
    "education_num",
    "capital_gain",
    "capital_loss",
    "hours_per_week"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nNumeric Columns Converted")


# STEP 11: Handle Missing Values in Numerical Columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

print("\nNumerical Missing Values Filled")


# STEP 12: Handle Missing Values in Categorical Columns

categorical_columns = [
    "workclass",
    "education",
    "marital_status",
    "occupation",
    "relationship",
    "race",
    "sex",
    "native_country",
    "income"
]

for col in categorical_columns:
    df[col] = df[col].fillna("Unknown")

print("\nCategorical Missing Values Filled")


# STEP 13: Check Missing Values Again

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# STEP 14: Check Duplicate Values Again

print("\nRemaining Duplicate Rows:")
print(df.duplicated().sum())


# STEP 15: Final Dataset Information

print("\nFinal Dataset Information:")
print(df.info())


# STEP 16: Final Dataset Shape

print("\nFinal Dataset Shape:")
print(df.shape)


# STEP 17: Display Cleaned Dataset

print("\nCleaned Dataset:")
print(df.head(10))


# STEP 18: Save Cleaned Dataset

df.to_csv("Cleaned_Adult_Data.csv", index=False)

print("\n===================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("===================================")

print("Cleaned Dataset Saved Successfully!")
# ANALYSIS
#Total rows
#32,561

#Total columns
#15

#Duplicate rows
#24

#Missing values
#4,262
#Across three columns


#Missing values by column
#Column	Missing
#workclass	1,836
#occupation	1,843
#native_country	583
