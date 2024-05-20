import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests.exceptions import RequestException, HTTPError, ConnectionError, Timeout
import time
import logging
import random

def parse_content(content):
    """Parse content with BeautifulSoup, handling both raw HTML and HTTP response objects."""
    # Check if content has 'content' attribute (indicating it's an HTTP response object)
    if hasattr(content, 'content'):
        soup = BeautifulSoup(content.content, "html.parser")
    else:
        soup = BeautifulSoup(content, "html.parser")
    
    return soup
    
def get_random_headers():
    """Generate random headers for the request."""
    return {'User-Agent': UserAgent().random}



def handle_errors(response, http_err):
    """Handle HTTP errors based on the response status code."""
    if response.status_code == 403:
        return "The site is protected by Cloudflare or other restrictions. Please try again later."
    elif response.status_code == 404:
        return "The page was not found. Please check the URL."
    else:
        return f"HTTP error occurred: {http_err}"

def pyparse(url, max_retries=5, delay=2, timeout=10):
    """
    Make a request to the specified URL, retrieve the HTML content,
    and parse it using BeautifulSoup.
    
    Args:
        url (str): The URL of the webpage to retrieve.
        max_retries (int): Maximum number of retries in case of failure.
        delay (int): Delay in seconds between retries.
        timeout (int): Timeout in seconds for the request.
    
    Returns:
        BeautifulSoup or dict: The parsed HTML content if successful, otherwise a dict with error information.
    """
    
    for attempt in range(max_retries):
        try:
            # Generate headers
            headers = get_random_headers()
            
            # Make the HTTP request with a timeout
            response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
            
            # Check if the request was successful
            response.raise_for_status()
            
            # Check if CAPTCHA is present in the response
            if "hcaptcha" in response.text or "recaptcha" in response.text:
                error_message = "CAPTCHA detected. Manual intervention required."
                logging.error(error_message)
                return {"error": error_message}
            
            return response
        except HTTPError as http_err:
            error_message = handle_errors(response, http_err)
            logging.error(error_message)
        except ConnectionError:
            error_message = "Connection error. Please check your internet connection."
            logging.error(error_message)
        except Timeout:
            error_message = "The request timed out. Please try again later."
            logging.error(error_message)
        except RequestException as req_err:
            error_message = f"An error occurred: {req_err}"
            logging.error(error_message)
        except Exception as err:
            error_message = f"An unexpected error occurred: {err}"
            logging.error(error_message)
        
        if attempt < max_retries - 1:
            time.sleep(delay + random.uniform(0, 2))  # Adding a random delay to avoid being blocked
        else:
            logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
            return {"error": error_message}
