import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def predict_price(area, bedrooms, bathrooms, age):
    data = {
        'Area': [800, 1000, 1200, 1500, 1800],
        'Bedrooms': [2, 2, 3, 3, 4],
        'Bathrooms': [1, 2, 2, 3, 3],
        'Age': [15, 10, 8, 5, 2],
        'Price': [3000000, 4000000, 5000000, 6500000, 8000000]
    }

    df = pd.DataFrame(data)

    X = df[['Area', 'Bedrooms', 'Bathrooms', 'Age']]
    y = df['Price']

    model = LinearRegression()
    model.fit(X, y)

    new_house = np.array([[area, bedrooms, bathrooms, age]])
    return int(model.predict(new_house)[0])
