import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
data = {
    'Area': [800, 1000, 1200, 1500, 1800],
    'Bedrooms': [2, 2, 3, 3, 4],
    'Bathrooms': [1, 2, 2, 3, 3],
    'Age': [15, 10, 8, 5, 2],
    'Price': [3000000, 4000000, 5000000, 6500000, 8000000]
}
df = pd.DataFrame(data)
print(df)
X = df[['Area', 'Bedrooms', 'Bathrooms', 'Age']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1
)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))
new_house = [[1400, 3, 2, 6]]
price = model.predict(new_house)

print("Predicted Price:", price[0])
