#main.py 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

def main():
    df = pd.read_csv("Housing_processed.csv")
    X = df.drop("price", axis=1)
    Y = df["price"]

    x_train, x_test, y_train, y_test = train_test_split(
            X, Y,
            test_size=0.2,
            random_state=9
            )
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    model = LinearRegression()

    model.fit(x_train_scaled, y_train)

    y_pred = model.predict(x_test_scaled)

    print("MSE: ", mean_squared_error(y_test, y_pred))
    print("MAE: ", mean_absolute_error(y_test, y_pred))
    print("R2 Score: ", r2_score(y_test, y_pred))


if __name__ == "__main__":
    main()
