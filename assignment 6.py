import os
import pandas as pd
import numpy as np


def load_data(file_path):
    """
    Loads dataset from a CSV or Excel (.xls, .xlsx) file into a pandas DataFrame.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".csv":
        df = pd.read_csv(file_path)
    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format! Please provide a .csv, .xls, or .xlsx file.")

    print(f"Successfully loaded dataset '{file_path}' with shape: {df.shape}")
    return df


def preprocess_data(df):
    """
    Performs standard data preprocessing:
    1. Removes duplicate rows
    2. Handles missing values (numeric & categorical)
    3. Trims whitespaces from string columns
    4. Detects and handles categorical encoding
    """
    print("\n--- Initial Data Overview ---")
    print(df.info())
    print("\nMissing Values per Column:\n", df.isnull().sum())

    # 1. Remove duplicate rows
    duplicates_count = df.duplicated().sum()
    if duplicates_count > 0:
        df = df.drop_duplicates()
        print(f"\n[+] Removed {duplicates_count} duplicate row(s).")

    # 2. Trim leading/trailing whitespace in string columns
    str_cols = df.select_dtypes(include=["object"]).columns
    for col in str_cols:
        df[col] = df[col].astype(str).str.strip()

    # 3. Handle missing values
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if pd.api.types.is_numeric_dtype(df[col]):
                # Fill missing numeric values with median
                median_val = df[col].median()
                df[col] = df[col].fillna(median_val)
                print(f"[+] Filled missing values in numeric column '{col}' with median ({median_val}).")
            else:
                # Fill missing categorical values with mode
                mode_val = df[col].mode()[0] if not df[col].mode().empty else "Unknown"
                df[col] = df[col].fillna(mode_val)
                print(f"[+] Filled missing values in categorical column '{col}' with mode ('{mode_val}').")

    # 4. One-Hot Encoding for categorical features
    categorical_cols = df.select_dtypes(include=["object"]).columns
    if len(categorical_cols) > 0:
        print(f"\n[+] One-hot encoding categorical columns: {list(categorical_cols)}")
        df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    return df


def save_cleaned_data(df, output_path="cleaned_dataset.csv"):
    """
    Saves the processed DataFrame to a CSV file.
    """
    df.to_csv(output_path, index=False)
    print(f"\nCleaned dataset saved successfully as '{output_path}' with shape: {df.shape}")


def create_sample_file(filename="sample_dataset.csv"):
    """
    Creates a sample CSV file for testing purposes if no file is provided.
    """
    data = {
        "Age": [25, 30, np.nan, 35, 30, 40],
        "Salary": [50000, 60000, 55000, np.nan, 60000, 80000],
        "Department": ["IT", "HR", "IT", "Finance", "HR", np.nan],
        "Experience": [2, 5, 3, 8, 5, 12]
    }
    sample_df = pd.DataFrame(data)
    sample_df.to_csv(filename, index=False)
    print(f"Sample dataset created: '{filename}'")


if __name__ == "__main__":
    # Create dummy data for testing (Replace 'sample_dataset.csv' with your file path)
    test_file = "sample_dataset.csv"
    create_sample_file(test_file)

    # 1. Load Data
    raw_df = load_data(test_file)

    # 2. Preprocess Data
    cleaned_df = preprocess_data(raw_df)

    # 3. Save Output
    save_cleaned_data(cleaned_df, "preprocessed_output.csv")
