'''from bs4 import BeautifulSoup
import requests

def scrape_url(url):
    print(f"Scraping the URL: {url}")
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch URL")
    soup = BeautifulSoup(response.text, 'html.parser')
    return {"title": soup.title.string, "content": soup.get_text()}
'''
from bs4 import BeautifulSoup
import requests

def scrape_url(url):
    print(f"Scraping the URL: {url}")
    
    try:
        # Sending a GET request to fetch the webpage
        response = requests.get(url)
        
        # Check if the response status code indicates success
        if response.status_code != 200:
            raise Exception(f"Failed to fetch URL. Status code: {response.status_code}")
        
        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract the title of the page
        title = soup.title.string if soup.title else 'No Title Found'
        print(f"Title: {title}")  # Debugging output
        
        # Extract the meta description (if available)
        meta_description = None
        if soup.find('meta', attrs={'name': 'description'}):
            meta_description = soup.find('meta', attrs={'name': 'description'})['content']
        
        # Extract headers (h1, h2, h3 tags)
        headers = [header.get_text().strip() for header in soup.find_all(['h1', 'h2', 'h3'])]
        print(f"Headers: {headers}")  # Debugging output
        
        # Get the main content of the page (all text)
        content = soup.get_text().strip()
        
        # If the content is too long, trim it for better readability
        if len(content) > 500:
            content = content[:500] + '...'
        
        # Return the data as a dictionary
        return {
            "title": title,
            "meta_description": meta_description,
            "headers": headers,
            "content": content
        }
    
    except requests.exceptions.RequestException as e:
        # Catch any request-related exceptions (e.g., connection errors)
        print(f"Error with the request: {e}")
        raise
    
    except Exception as e:
        # Catch any other general exceptions
        print(f"Error during scraping: {e}")
        raise
