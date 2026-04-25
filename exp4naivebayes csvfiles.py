import pandas as pd
from sklearn.model_selection import train_test_split from sklearn.naive_bayes
import GaussianNB
from sklearn.preprocessing import LabelEncoder from sklearn.metrics
import accuracy_score import matplotlib.pyplot as plt
# 1. LOAD DATA
data = pd.read_csv('temp_hum_play_data.csv') # 2. ENCODE
TARGET COLUMN ONLY (Play)
le = LabelEncoder()
data['Play'] = le.fit_transform(data['Play']) # No = 0, Yes = 1
# 3. SPLIT FEATURES AND TARGET
X = data[['Temperature', 'Humidity']] y = data['Play']

# 4. TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.2, random_state=42 )
# 5. TRAIN GAUSSIAN NAIVE BAYES
model = GaussianNB() model.fit(X_train,
y_train)
# 6. PREDICT
prediction = model.predict(X_test) # Predict for
entire dataset all_predictions = model.predict(X)
# 7. ACCURACY
print("Accuracy:", accuracy_score(y_test, prediction)) # 8. SHOW LEARNED
PARAMETERS
print("\nClass Priors:", model.class_prior_) print("\nMean (theta):\n",
model.theta_) print("\nVariance:\n", model.var_)
# 9. ACTUAL VS PREDICTED PLOT
plt.figure(figsize=(8,6)) # Actual
values
plt.scatter(X['Temperature'],
X['Humidity'], c=y,
cmap='coolwarm',
marker='o', label='Actual')
# Predicted values plt.scatter(X['Temperature'],

X['Humidity'],
c=all_predictions,
cmap='coolwarm',
marker='x', s=100,
label='Predicted')
plt.xlabel("Temperature")

plt.ylabel("Humidity")
plt.title("Actual vs Predicted (All Data)") plt.legend()
plt.show()
