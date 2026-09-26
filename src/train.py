import os
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from src.data_processing import load_data
from src.feature_engineering import create_features
from pathlib import Path

def train_model(data_path, model_path):
    # Load data
    df=load_data(data_path)
    X, y = create_features(df)
    
    X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    #Prediction
    y_pred = model.predict(X_test)
    
    # Evaluate
    mae = mean_absolute_error(y_test, y_pred)
    rmse=mean_squared_error(y_test, y_pred) ** 0.5
    r2 = r2_score(y_test, y_pred)
    
    print(mae)
    print(rmse)
    print(r2)
    
    # save model
    model_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )
    joblib.dump(model, model_path)
    print(model_path)
    
if __name__ == "__main__":
    # Project root
    BASE_DIR=Path(__file__).resolve().parent.parent
    
    data_path=(BASE_DIR/"data"/"processed"/"cleaned_housing.csv")  
    model_path=(BASE_DIR/"models"/"final_model.pkl")
    train_model(
        data_path,
        model_path
    ) 
    