import os
import requests
from bs4 import BeautifulSoup

# Set the URL of the website you want to scrape
url = 'https://www.icai.org/post.html?post_id=17822'

# Send an HTTP GET request to the website and retrieve the response
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the links on the page that link to a PDF file
pdf_links = soup.find_all('a', href=lambda href: href.endswith('.pdf'))

# Set the destination directory where the PDF files will be saved
destination_directory = 'D:\Python'

# Iterate over the links and download each PDF file
for link in pdf_links:
  # Construct the full URL of the PDF file
  pdf_url = link['href']

  # Download the PDF file
  response = requests.get(pdf_url)

  # Extract the filename from the URL
  pdf_filename = pdf_url.split('/')[-1]

  # Save the PDF file to the destination directory
  with open(os.path.join(destination_directory, pdf_filename), 'wb') as f:
    f.write(response.content)

print('Finished downloading PDF files')