# Import the necessary libraries
import pandas as pd

# Define the input and output file names
input_file = 'input.csv'
output_file = 'output.csv'

# Read the input CSV file
df = pd.read_csv(input_file).head(1)

# Combine the First_Name and Last_Name columns into a single column called Name
df['Name'] = df['First_Name'] + ' ' + df['Last_Name']

# Select the ID and Name columns and create a new DataFrame
new_df = df[['ID', 'Name']]

# Write the new DataFrame to a CSV file
new_df.to_csv(output_file, index=False)

print(f"Output file saved to {output_file}")