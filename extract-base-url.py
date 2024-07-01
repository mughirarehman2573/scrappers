import pandas as pd
import urllib.parse


def extract_base_url(original_url):
    # Parse the original URL
    parsed_url = urllib.parse.urlparse(original_url)

    # Extract base URL
    base_url = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path

    return base_url


# Read the CSV file
df = pd.read_csv('grade-cracker-08-05-formatted.csv')

# Extract base URL from each URL and create a new column with base URLs
df['Base URL'] = df['Apply Now Link'].apply(extract_base_url)

# Save the base URLs into a separate CSV file
df[['Base URL']].to_csv('base_urls.csv', index=False)
