import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

def load_data():
    df = pd.read_csv(BASE_DIR / "sales_data.csv")
    return df

def clean_data(df):
    df = df.drop_duplicates()

    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")

    df = df.dropna()
    df = df[(df["Quantity"] > 0) & (df["Unit_Price"] >= 0)]

    df["Sales"] = df["Quantity"] * df["Unit_Price"]

    return df

def analyze_data(df):
    total_sales = df["Sales"].sum()
    total_quantity = df["Quantity"].sum()
    average_sales = df["Sales"].mean()

    product_sales = df.groupby("Product")["Sales"].sum()
    monthly_sales = df.groupby(
        df["Date"].dt.to_period("M")
    )["Sales"].sum()

    return total_sales, total_quantity, average_sales, product_sales, monthly_sales

def visualize_data(product_sales, monthly_sales):

    plt.figure(figsize=(8, 5))
    product_sales.plot(kind="bar")
    plt.title("Sales by Product")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "bar_chart.png")
    plt.show()

    plt.figure(figsize=(8, 5))
    monthly_sales.index = monthly_sales.index.astype(str)
    monthly_sales.plot(kind="line", marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid()
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "line_chart.png")
    plt.show()

def create_report(df, total_sales, total_quantity,
                  average_sales, product_sales, monthly_sales):

    report = f"""
SALES DATA ANALYSIS REPORT
==========================

Total Revenue: Rs. {total_sales:,.2f}
Total Records: {len(df)}
Total Items Sold: {total_quantity}
Average Sales: Rs. {average_sales:,.2f}

PRODUCT-WISE SALES
{product_sales.to_string()}

MONTHLY SALES
{monthly_sales.to_string()}

KEY INSIGHTS
1. Highest Sales Product: {product_sales.idxmax()}
2. Highest Sales Month: {monthly_sales.idxmax()}
3. Total Revenue: Rs. {total_sales:,.2f}
"""

    with open(OUTPUT_DIR / "report.txt", "w") as file:
        file.write(report)

    print(report)

def main():
    try:
        df = load_data()
        print("Data Loaded Successfully")

        df = clean_data(df)
        print("Data Cleaned Successfully")

        results = analyze_data(df)

        total_sales, total_quantity, average_sales, product_sales, monthly_sales = results

        print("Total Revenue:", total_sales)
        print("Total Items:", total_quantity)
        print("Average Sales:", average_sales)

        visualize_data(product_sales, monthly_sales)

        create_report(
            df, total_sales, total_quantity,
            average_sales, product_sales, monthly_sales
        )

        df.to_csv(OUTPUT_DIR / "cleaned_data.csv", index=False)

        print("Analysis Completed Successfully")

    except FileNotFoundError:
        print("Error: sales_data.csv file not found")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()