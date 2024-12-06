import requests
from PIL import Image
from io import BytesIO
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Your Cat API key
API_KEY = "live_EJAF38z97DdGmsMCE8kJIXKsGH6sY6zlU4Lw43cyh9ujEQWP16qeGBQgx1Zc830o"

# Function to fetch and display a random cat image
def fetch_and_show_cat():
    try:
        # API endpoint
        url = "https://api.thecatapi.com/v1/images/search"
        headers = {"x-api-key": API_KEY}

        # Make the API request
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the response
        cat_data = response.json()
        cat_image_url = cat_data[0]["url"]

        # Fetch the cat image
        img_response = requests.get(cat_image_url)
        img_response.raise_for_status()
        img_data = BytesIO(img_response.content)

        # Open the cat image
        img = Image.open(img_data)
        img.show()

        print("Enjoy your cat image! 🐾")
    except Exception as e:
        print("Error fetching cat image 😺")
        print(f"Details: {e}")

# Run the function
if __name__ == "__main__":
    print("Fetching a random cat image... 🐾")
    fetch_and_show_cat()
