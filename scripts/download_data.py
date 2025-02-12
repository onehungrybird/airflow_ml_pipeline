import pandas as pd
from sklearn.datasets import load_iris

def download_data():
    """Downloads and preprocesses the dataset."""
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    df.to_csv("data/iris.csv", index=False)
    print("✅ Data saved successfully!")

if __name__ == "__main__":
    download_data()
