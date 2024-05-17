import requests 
from bs4 import BeautifulSoup 
from fake_useragent import UserAgent 
from requests.exceptions import RequestException

def pyparse(url, max_retries=1):
    """
    Make a request to the specified URL, retrieve the HTML content,
    and parse it using BeautifulSoup.
    
    Args:
        url (str): The URL of the webpage to retrieve.
        max_retries (int): Maximum number of retries in case of failure.
    
    Returns:
        BeautifulSoup or None: The parsed HTML content if successful, otherwise None.
    """
    for attempt in range(max_retries):
        try:
            # Generate a random user agent
            headers = {'User-Agent': UserAgent().random}
            
            # Make the HTTP request
            response = requests.get(url, headers=headers)
            
            # Check if the request was successful
            response.raise_for_status()
            
            # Parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")
            return soup
        except RequestException as e:
            print(f"Failed to retrieve content from {url}. Error: {e}")
            if attempt < max_retries - 1:
                print("Retrying...")
            else:
                print("Maximum retries reached. Giving up.")
                return None
