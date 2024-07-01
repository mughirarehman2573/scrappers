import csv
from urllib.parse import urlparse, parse_qs


def extract_desired_link(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    desired_link = query_params['u'][0]

    # Remove URL encoding from the extracted link
    desired_link = desired_link.replace('%25', '%').replace('%3A', ':').replace('%2F', '/')

    return desired_link


# Read URLs from CSV file
input_csv_file = 'grade-cracker-08-05-formatted.csv'  # Replace 'input_file.csv' with the path to your input CSV file
output_csv_file = 'output_link-file.csv'  # Replace 'output_file.csv' with the path to your output CSV file
column_name = 'Apply Now Link'

with open(input_csv_file, 'r', newline='') as input_file, \
        open(output_csv_file, 'w', newline='') as output_file:
    reader = csv.DictReader(input_file)
    writer = csv.writer(output_file)

    # Write header to the output file
    writer.writerow(["Desired Link"])

    for row in reader:
        url = row[column_name]
        desired_link = extract_desired_link(url)
        writer.writerow([desired_link])

print("Extraction and writing to CSV completed.")
