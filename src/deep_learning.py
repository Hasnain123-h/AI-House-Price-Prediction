from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
    
def train_ann(data_path, model_path, scaler_path):
    df = pd.read_csv(data_path)
    X = df.drop("median_house_value", axis=1)
    y = df["median_house_value"]

    X = pd.get_dummies(
        X,
        columns=["ocean_proximity"],
        dtype=int
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
   
    model = Sequential([
        Dense(
            128,
            activation="relu",
            input_shape=(X_train_scaled.shape[1],)
        ),
        Dense(64, activation="relu"),
        Dense(1)
    ])

    model.compile(
        optimizer="adam",
        loss="mean_squared_error",
        metrics=["mae"]
    )

    model.fit(
        X_train_scaled,
        y_train,
        validation_split=0.2,
        epochs=100,
        batch_size=32,
        verbose=1
    )
    

    y_pred = model.predict(X_test_scaled, verbose=0).flatten()


    mae = mean_absolute_error(y_test, y_pred)

    rmse = np.sqrt(
    mean_squared_error(y_test, y_pred)
)

    r2 = r2_score(
    y_test,
    y_pred
)

    print("\nANN Evaluation")
    print("MAE:", mae)
    print("RMSE:", rmse)
    print("R2 Score:", r2)

    model_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    model.save(model_path)
    joblib.dump(scaler, scaler_path)

    print("ANN training completed!")
    print("Model saved:", model_path)
    print("Scaler saved:", scaler_path)


if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent
    data_path = (BASE_DIR / "data" / "processed" / "cleaned_housing.csv")
    model_path = (BASE_DIR / "models" / "ann_house_price_model.keras")
    scaler_path = (BASE_DIR / "models" / "ann_scaler.pkl")
    print("Callingvtrain_ann function")
    train_ann(
        data_path,
        model_path,
        scaler_path
    )


   
    
    

    
    
    


