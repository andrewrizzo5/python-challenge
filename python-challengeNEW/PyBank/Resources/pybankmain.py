import pandas as pd

# Load the data from the CSV file
file_path = open('budget_data.csv')
budget_data = pd.read_csv(file_path)

# Calculate the total number of months
total_months = budget_data.shape[0]

# Calculate the net total amount of "Profit/Losses"
total_profit_losses = budget_data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses"
budget_data['Change'] = budget_data['Profit/Losses'].diff()

# Calculate the average of those changes
average_change = budget_data['Change'].mean()

# Find the greatest increase in profits
max_increase = budget_data.loc[budget_data['Change'].idxmax()]

# Find the greatest decrease in profits
max_decrease = budget_data.loc[budget_data['Change'].idxmin()]

# Results
total_months, total_profit_losses, average_change, max_increase['Date'], max_increase['Change'], max_decrease['Date'], max_decrease['Change']

# Formatting and printing the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {max_increase['Date']} (${max_increase['Change']})")
print(f"Greatest Decrease in Profits: {max_decrease['Date']} (${max_decrease['Change']})")

import csv

# Define the data to be written to the CSV
rows = [
    ["Description", "Value"],
    ["Total Months", total_months],
    ["Total", f"${total_profit_losses}"],
    ["Average Change", f"${average_change:.2f}"],
    ["Greatest Increase in Profits", f"{max_increase['Date']} (${max_increase['Change']})"],
    ["Greatest Decrease in Profits", f"{max_decrease['Date']} (${max_decrease['Change']})"]
]

# Specify the CSV file name
csv_file_name = 'financial_analysis.csv'

# Writing to CSV
with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

