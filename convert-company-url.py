import pandas as pd

# Read the CSV file
df = pd.read_csv('grade-cracker-08-05-formatted.csv')

# Add a new column 'company_url' by combining 'https://www.' with 'company_name' and '.com'
df['company_url'] = 'https://www.' + df['company_name'] + '.com/'

# Write the modified data back to the CSV file
df.to_csv('grade-cracker-16-05-2023.csv', index=False)
