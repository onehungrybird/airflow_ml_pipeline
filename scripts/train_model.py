import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model():
    """Loads data, trains a model, and saves it."""
    df = pd.read_csv("data/iris.csv")
    X = df.drop(columns=['target'])
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    with open("models/iris_model.pkl", "wb") as f:
        pickle.dump(model, f)
    
    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train_model()
