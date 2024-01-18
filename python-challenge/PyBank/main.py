import pandas as pd

# Load the data from the CSV file
file_path = '/python-challenge/PyBank/budget_data.csv'
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
