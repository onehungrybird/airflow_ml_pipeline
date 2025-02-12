import pandas as pd
import pickle
from sklearn.metrics import accuracy_score

def evaluate_model():
    """Loads trained model, evaluates it, and logs accuracy."""
    df = pd.read_csv("data/iris.csv")
    X = df.drop(columns=['target'])
    y = df['target']
    
    with open("models/iris_model.pkl", "rb") as f:
        model = pickle.load(f)
    
    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    
    with open("logs/metrics.txt", "w") as f:
        f.write(f"Accuracy: {accuracy:.4f}")
    
    print(f"✅ Model accuracy: {accuracy:.4f}")

if __name__ == "__main__":
    evaluate_model()
