# read data from web

import requests
from bs4 import BeautifulSoup

url = input("Enter the url with https:// ")

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the web page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extract and print the title of the web page
    title = soup.title.string
    print(f"Title: {title}")
    
    # Extract and print all the links on the web page
    links = soup.find_all('a')
    for link in links:
        print(f"Link: {link.get('href')}")
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)