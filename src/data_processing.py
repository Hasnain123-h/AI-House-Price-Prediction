import pandas as pd
from pathlib import Path
def load_data(file_path):
    """
    Load a CSV dataset into a Padas DataFrame
    """
    df = pd.read_csv(file_path)
    return df




if __name__=="__main__":
    # Project root directory
    BASE_DIR = Path(__file__).resolve().parent.parent
    file_path=BASE_DIR/"data"/"processed"/"cleaned_housing.csv"
    df = load_data(file_path)
    print(df.shape)
    print(df.head())