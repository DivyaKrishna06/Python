import requests

# Define the URL you want to access
url = 'https://example.com'

try:
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Print the content of the web page
        print(response.text)
    else:
        print(f'Failed to retrieve data. Status code: {response.status_code}')

except requests.exceptions.RequestException as e:
    print(f'An error occurred: {e}')

# You can now process the content of the web page as needed