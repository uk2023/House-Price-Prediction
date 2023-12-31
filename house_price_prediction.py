# -*- coding: utf-8 -*-
"""House-price-prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19_27qS5SMcV1jPzV_kxG64XeHRZ7a6xO
"""

#Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

#Load the California Housing dataset
california = fetch_california_housing()
data = pd.DataFrame(california.data, columns=california.feature_names)
target = pd.DataFrame(california.target, columns=['MEDV'])

#Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=42)

#Create a Linear Regression model
model = LinearRegression()

#Fit the model to the training data
model.fit(X_train, y_train)

#Make predictions on the test set
y_pred = model.predict(X_test)

#Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

#Print the model's performance metrics
print("House Price Prediction Model")
print("----------------------------")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2): {r2:.2f}")
print("----------------------------")
print("Model Training Complete.")

#Visualize the results with scatter plot
plt.figure(figsize=(12, 6))

#Scatter plot of actual vs. predicted house prices
plt.subplot(1, 2, 1)
plt.scatter(y_test, y_pred)
plt.xlabel("Actual House Prices")
plt.ylabel("Predicted House Prices")
plt.title("Actual Prices vs. Predicted Prices")

#Histogram of the differences between real and predicted prices
plt.subplot(1, 2, 2)
plt.hist(y_test - y_pred, bins=30)
plt.xlabel("Price Difference")
plt.ylabel("Frequency")
plt.title("Difference between Actual and Predicted Prices")

plt.tight_layout()
plt.show()

