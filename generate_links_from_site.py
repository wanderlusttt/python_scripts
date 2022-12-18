import requests
from bs4 import BeautifulSoup

# Set the URL of the website you want to scrape
url = 'https://www.icai.org/post.html?post_id=17822'

# Send an HTTP GET request to the website and retrieve the response
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the links on the page that link to a file
file_links = soup.find_all('a', href=True)

# Iterate over the links and print the text and the URL of each link
for link in file_links:
  print(link.text + ': ' + link['href'])
  
