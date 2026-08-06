"""Restaurant tips data analysis with pandas & Matplotlib.

Reads the classic restaurant tips dataset and produces charts and key
findings for the analytics portfolio. Run with:

    python analysis.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "tips.csv"
OUTPUT_DIR = BASE_DIR / "output"


def load_data() -> pd.DataFrame:
    """Load the tips dataset from the committed CSV."""
    return pd.read_csv(DATA_PATH)


def chart_bill_distribution(df: pd.DataFrame) -> Path:
    """Histogram of total bill amounts."""
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.hist(df["total_bill"], bins=20, edgecolor="white", color="#4c72b0")
    ax.set_title("Distribution of total bills")
    ax.set_xlabel("Total bill (ZAR equivalent)")
    ax.set_ylabel("Number of visits")
    fig.tight_layout()
    path = OUTPUT_DIR / "bill_distribution.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def chart_avg_tip_by_day(df: pd.DataFrame) -> Path:
    """Average tip per day of the week."""
    order = ["Thur", "Fri", "Sat", "Sun"]
    avg = df.groupby("day")["tip"].mean().reindex(order)
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.bar(avg.index, avg.values, color="#55a868")
    ax.set_title("Average tip by day")
    ax.set_xlabel("Day")
    ax.set_ylabel("Average tip")
    for i, value in enumerate(avg.values):
        ax.text(i, value + 0.05, f"{value:.2f}", ha="center", fontsize=9)
    fig.tight_layout()
    path = OUTPUT_DIR / "avg_tip_by_day.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def chart_bill_vs_tip(df: pd.DataFrame) -> Path:
    """Scatter of total bill vs tip, coloured by party size."""
    fig, ax = plt.subplots(figsize=(8, 4.5))
    scatter = ax.scatter(
        df["total_bill"],
        df["tip"],
        c=df["size"],
        cmap="viridis",
        alpha=0.8,
        edgecolor="white",
    )
    ax.set_title("Total bill vs tip, by party size")
    ax.set_xlabel("Total bill")
    ax.set_ylabel("Tip")
    fig.colorbar(scatter, ax=ax, label="Party size")
    fig.tight_layout()
    path = OUTPUT_DIR / "bill_vs_tip.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def chart_tip_percentage_by_time(df: pd.DataFrame) -> Path:
    """Box plot of tip percentage by meal time."""
    df = df.copy()
    df["tip_pct"] = df["tip"] / df["total_bill"] * 100
    fig, ax = plt.subplots(figsize=(8, 4.5))
    df.boxplot(column="tip_pct", by="time", ax=ax, grid=False)
    ax.set_title("Tip percentage by meal time")
    ax.set_ylabel("Tip (%)")
    fig.suptitle("")
    fig.tight_layout()
    path = OUTPUT_DIR / "tip_pct_by_time.png"
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def print_findings(df: pd.DataFrame) -> None:
    """Print the key findings from the analysis."""
    df = df.copy()
    df["tip_pct"] = df["tip"] / df["total_bill"] * 100
    print("=== Key findings ===")
    print(f"Visits analysed: {len(df)}")
    print(f"Average total bill: {df['total_bill'].mean():.2f}")
    print(f"Average tip: {df['tip'].mean():.2f}")
    print(f"Average tip percentage: {df['tip_pct'].mean():.1f}%")
    print(f"Most common day: {df['day'].mode()[0]}")
    print(f"Most common meal time: {df['time'].mode()[0]}")


def main() -> None:
    """Run the full analysis and save all charts."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    df = load_data()
    print_findings(df)
    chart_bill_distribution(df)
    chart_avg_tip_by_day(df)
    chart_bill_vs_tip(df)
    chart_tip_percentage_by_time(df)
    print(f"Charts saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
