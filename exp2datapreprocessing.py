import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
# --- STEP 1: LOAD DATA (Creating a dummy dataset for the lab) ---
data = {
'Country': ['India', 'USA', 'India', 'USA', 'UK', 'India'],
'Age': [22, 25, np.nan, 30, 28, 35], # Note the 'nan' (missing value)
'Salary': [40000, 60000, 50000, np.nan, 72000, 58000],
'Purchased': ['No', 'Yes', 'Yes', 'No', 'Yes', 'Yes']
}
df = pd.DataFrame(data)
print("--- ORIGINAL RAW DATA ---")
print(df)
print("\n")
Check for missing values
print("--- MISSING VALUES COUNT ---")
print(df.isnull().sum())
print("\n")
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print("--- DATA AFTER CLEANING ---")
print(df)
print("\n")
df_encoded = pd.get_dummies(df, columns=['Country'])
# For the Target column (Purchased), let's map Yes/No manually
df_encoded['Purchased'] = df_encoded['Purchased'].map({'Yes': 1, 'No':
0})
print("--- DATA AFTER ENCODING (All Numbers Now) ---")
print(df_encoded)
print("\n")
# Logic: Age is 20-30, Salary is 40000-60000. Salary dominates Age
because it's bigger.
# We shrink them to the same scale.
# Separate Features (X) and Target (y)
X = df_encoded.drop('Purchased', axis=1)
y = df_encoded['Purchased']
# Scale
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
print("--- FINAL PROCESSED DATA (Ready for AI) ---")
print(pd.DataFrame(X_scaled, columns=X.columns).head())
