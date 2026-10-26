import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def create_sample_csv(filename="dataset.csv"):
    """
    Creates a sample CSV file for demonstration if no file exists.
    """
    data = {
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug"],
        "Temperature": [15, 18, 22, 26, 30, 33, 35, 34],
        "Ice_Cream_Sales": [1200, 1500, 2300, 3400, 4800, 5600, 6200, 5900],
        "Foot_Traffic": [800, 950, 1100, 1400, 1800, 2100, 2300, 2200],
        "Marketing_Spend": [500, 600, 750, 900, 1200, 1300, 1500, 1400]
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Sample dataset created: '{filename}'")


def visualize_data(file_path):
    """
    Loads a CSV file and generates Line, Bar, Scatter, and Heatmap plots.
    """
    # 1. Load Dataset
    df = pd.read_csv(file_path)
    print("\nDataset loaded successfully:")
    print(df.head())

    # Set up plot grid (2 rows, 2 columns)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Dataset Visualizations", fontsize=16, fontweight="bold")

    # -------------------------------------------------------------
    # Plot 1: Line Plot (Temperature over Months)
    # -------------------------------------------------------------
    axes[0, 0].plot(df["Month"], df["Temperature"], marker="o", color="#1f77b4", linewidth=2)
    axes[0, 0].set_title("1. Line Plot: Temperature Trend")
    axes[0, 0].set_xlabel("Month")
    axes[0, 0].set_ylabel("Temperature (°C)")
    axes[0, 0].grid(True, linestyle="--", alpha=0.6)

    # -------------------------------------------------------------
    # Plot 2: Bar Plot (Ice Cream Sales per Month)
    # -------------------------------------------------------------
    axes[0, 1].bar(df["Month"], df["Ice_Cream_Sales"], color="#ff7f0e", edgecolor="black")
    axes[0, 1].set_title("2. Bar Plot: Ice Cream Sales")
    axes[0, 1].set_xlabel("Month")
    axes
