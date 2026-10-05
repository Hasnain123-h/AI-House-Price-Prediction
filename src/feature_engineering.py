from pathlib import Path
import pandas as pd

TARGET_COLUMN = "median_house_value"
CATEGORICAL_COLUMN = "ocean_proximity"

def create_features(df):    
    X = df.drop(TARGET_COLUMN, axis=1)
    y = df[TARGET_COLUMN]

    X = pd.get_dummies(
        X,
        columns=[CATEGORICAL_COLUMN],
        dtype=int
    )

    return X, y


def prepare_input(input_data, feature_columns):    
    input_data = pd.get_dummies(
        input_data,
        columns=[CATEGORICAL_COLUMN],
        dtype=int
    )

    # Make sure all training columns exist
    input_data = input_data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    return input_data

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent
    file_path = (BASE_DIR/ "data"/ "processed" / "cleaned_housing.csv")
    df = pd.read_csv(file_path)
    X, y = create_features(df)

    print("Feature engineering completed!")
    print("Features shape:", X.shape)
    print("Target shape:", y.shape)
    print("\nFeature columns:")
    print(X.columns.tolist())