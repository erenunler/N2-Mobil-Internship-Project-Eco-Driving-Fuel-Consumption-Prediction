# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

def load_and_split_data(file_path):
    df = pd.read_csv(file_path)
    X = df.drop('fuel_consumption', axis=1)
    y = df['fuel_consumption']

    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.30, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.50, random_state=42)

    return X_train, X_val, X_test, y_train, y_val, y_test

def evaluate_model(model, X, y, dataset_name):
    predictions = model.predict(X)
    mae = mean_absolute_error(y, predictions)
    rmse = np.sqrt(mean_squared_error(y, predictions))
    r2 = r2_score(y, predictions)

    print(f"--- {dataset_name} Sonuçları ---")
    print(f"MAE: {mae:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R2 Skoru: {r2:.4f}\n")

    return mae, rmse, r2

def main():
    print("Veri yükleniyor ve bölünüyor...")
    file_path = '/content/drive/MyDrive/eco_driving_score_cleaned.csv'
    X_train, X_val, X_test, y_train, y_val, y_test = load_and_split_data(file_path)

    best_params = {
        'n_estimators': 100,
        'min_samples_split': 2,
        'min_samples_leaf': 4,
        'max_depth': 4,
        'learning_rate': 0.05
    }

    model = GradientBoostingRegressor(**best_params, random_state=42)

    print("Model eğitiliyor...")
    model.fit(X_train, y_train)

    evaluate_model(model, X_train, y_train, "Eğitim Seti")
    evaluate_model(model, X_val, y_val, "Doğrulama Seti")

    joblib.dump(model, '/content/drive/MyDrive/models/gradient_boosting_model.pkl')
    print("Model başarıyla kaydedildi.")

if __name__ == "__main__":
    main()
