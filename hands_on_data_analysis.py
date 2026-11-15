"""
HANDS-ON PRACTICE: COMPLETE DATA ANALYSIS PROJECT

Requirements covered:
1. Bar chart showing sales by product category
2. Line chart showing monthly temperature changes
3. Pie chart showing expense distribution
4. Professional chart titles and labels
5. Data loading, cleaning, analysis and visualization
6. Complete report with numerical results and charts

Required libraries:
    pip install pandas matplotlib

Run:
    python hands_on_data_analysis.py

The program creates:
    sales_by_category.png
    monthly_temperature.png
    expense_distribution.png
    complete_analysis_report.txt
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def load_data():
    """Create and load the sample datasets."""
    sales = pd.DataFrame({
        "Category": ["Mobile", "Laptop", "Tablet", "Headphones"],
        "Sales": [25000, 45000, 15000, 10000]
    })

    temperature = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Temperature": [18, 21, 25, 30, 34, 32]
    })

    expenses = pd.DataFrame({
        "Expense": ["Food", "Travel", "Rent", "Shopping"],
        "Amount": [5000, 2000, 8000, 3000]
    })

    print("1. DATA LOADED SUCCESSFULLY")
    return sales, temperature, expenses


def clean_data(sales, temperature, expenses):
    """Remove missing and duplicate rows and validate numeric values."""
    sales = sales.dropna().drop_duplicates().copy()
    temperature = temperature.dropna().drop_duplicates().copy()
    expenses = expenses.dropna().drop_duplicates().copy()

    if (sales["Sales"] < 0).any():
        raise ValueError("Sales values cannot be negative.")
    if (temperature["Temperature"] < 0).any():
        raise ValueError("Temperature values cannot be negative.")
    if (expenses["Amount"] < 0).any():
        raise ValueError("Expense values cannot be negative.")

    print("2. DATA CLEANING AND VALIDATION COMPLETED")
    return sales, temperature, expenses


def analyze_data(sales, temperature, expenses):
    """Calculate important numerical results."""
    results = {
        "total_sales": sales["Sales"].sum(),
        "highest_sales_category": sales.loc[
            sales["Sales"].idxmax(), "Category"
        ],
        "average_temperature": temperature["Temperature"].mean(),
        "highest_temperature": temperature["Temperature"].max(),
        "total_expenses": expenses["Amount"].sum(),
        "highest_expense": expenses.loc[
            expenses["Amount"].idxmax(), "Expense"
        ]
    }

    print("\n3. DATA ANALYSIS")
    print("Total Sales:", results["total_sales"])
    print("Highest Sales Category:", results["highest_sales_category"])
    print("Average Temperature:", round(results["average_temperature"], 2), "°C")
    print("Highest Temperature:", results["highest_temperature"], "°C")
    print("Total Expenses:", results["total_expenses"])
    print("Highest Expense:", results["highest_expense"])
    return results


def create_charts(sales, temperature, expenses, output_folder):
    """Create and save three charts with titles and axis labels."""

    # Bar chart: sales by product category
    plt.figure(figsize=(8, 5))
    plt.bar(sales["Category"], sales["Sales"])
    plt.title("Sales by Product Category")
    plt.xlabel("Product Category")
    plt.ylabel("Sales Amount")
    plt.tight_layout()
    plt.savefig(output_folder / "sales_by_category.png", dpi=150)
    plt.show()
    plt.close()

    # Line chart: monthly temperature changes
    plt.figure(figsize=(8, 5))
    plt.plot(
        temperature["Month"],
        temperature["Temperature"],
        marker="o"
    )
    plt.title("Monthly Temperature Changes")
    plt.xlabel("Month")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_folder / "monthly_temperature.png", dpi=150)
    plt.show()
    plt.close()

    # Pie chart: expense distribution
    plt.figure(figsize=(7, 5))
    plt.pie(
        expenses["Amount"],
        labels=expenses["Expense"],
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Expense Distribution")
    plt.tight_layout()
    plt.savefig(output_folder / "expense_distribution.png", dpi=150)
    plt.show()
    plt.close()

    print("\n4. ALL THREE CHARTS CREATED AND SAVED")


def create_report(results, output_folder):
    """Save a text report containing numerical results and insights."""
    report = f"""
COMPLETE DATA ANALYSIS REPORT
=============================

DATA ANALYSIS RESULTS
---------------------
Total Sales: {results['total_sales']}
Highest Sales Category: {results['highest_sales_category']}
Average Temperature: {results['average_temperature']:.2f} °C
Highest Temperature: {results['highest_temperature']} °C
Total Expenses: {results['total_expenses']}
Highest Expense Category: {results['highest_expense']}

PROJECT INSIGHTS
----------------
1. {results['highest_sales_category']} has the highest sales.
2. The average temperature for the six months is
   {results['average_temperature']:.2f} °C.
3. {results['highest_expense']} is the highest expense category.

PROJECT WORKFLOW
----------------
Data Loading: Completed
Data Cleaning: Completed
Data Analysis: Completed
Data Visualization: Completed

CHART FILES
-----------
sales_by_category.png
monthly_temperature.png
expense_distribution.png

Project Status: Successfully Completed
"""
    report_path = output_folder / "complete_analysis_report.txt"
    report_path.write_text(report, encoding="utf-8")
    print(report)
    print("5. REPORT SAVED TO:", report_path)


def main():
    output_folder = Path(__file__).resolve().parent

    try:
        sales, temperature, expenses = load_data()
        sales, temperature, expenses = clean_data(
            sales, temperature, expenses
        )
        results = analyze_data(sales, temperature, expenses)
        create_charts(sales, temperature, expenses, output_folder)
        create_report(results, output_folder)

    except (ValueError, KeyError, OSError) as error:
        print("Project error:", error)
    except Exception as error:
        print("Unexpected error:", error)


if __name__ == "__main__":
    main()
