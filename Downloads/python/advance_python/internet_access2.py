import requests

def access_website(url):
    try:
        # Send an HTTP GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (HTTP status code 200)
        if response.status_code == 200:
            # Print the content of the website
            print("Website content:")
            print(response.text)
        else:
            print(f"Failed to access the website. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while accessing the website: {e}")

if __name__ == "__main__":
    # Replace this URL with the one you want to access
    website_url = "https://www.example.com"

    access_website(website_url)