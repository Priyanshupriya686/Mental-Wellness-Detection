import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

TARGET_COL = "18. How often do you feel depressed or down?"

def train_model(X, y, test_size=0.3, random_state=42):
    """
    Train a RandomForestClassifier on the data.

    Args:
        X (pd.DataFrame): Features.
        y (pd.Series): Target.
        test_size (float): Test split ratio.
        random_state (int): Random state.

    Returns:
        tuple: (model, X_train, X_test, y_train, y_test)
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    model = RandomForestClassifier(n_estimators=100, random_state=random_state)
    model.fit(X_train, y_train)

    return model, X_train, X_test, y_train, y_test

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model and print report.

    Args:
        model: Trained model.
        X_test: Test features.
        y_test: Test target.
    """
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    plt.figure(figsize=(5,4))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, cmap="Blues", fmt="d")
    plt.show()

def predict_depression_level(model, X):
    """
    Predict depression levels.

    Args:
        model: Trained model.
        X: Features.

    Returns:
        np.array: Predictions.
    """
    return model.predict(X)