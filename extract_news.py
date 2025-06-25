import requests
from bs4 import BeautifulSoup

# URL for general news
base_url = 'https://somoskudasai.com/noticias/'

def get_all_news_kudasai(base_url, limit=5):
    """
    Fetches the latest news links from Kudasai and returns up to `limit` URLs.

    Args:
        base_url (str): The URL of the Kudasai news page.
        limit (int): Maximum number of links to return (default is 5).

    Returns:
        List[str]: A list of up to `limit` extracted news URLs.
    """
    # 1. Request the page
    response = requests.get(base_url)
    response.raise_for_status()  # Raise an exception on HTTP errors

    # 2. Parse the response HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 3. Locate all <a> tags with the exact class attribute
    selector = 'a.py-1.hover\\:text-tone.hover\\:underline'
    anchors = soup.select(selector)

    # 4. Extract the href attributes, filter out None and non-string values
    links = []
    for a in anchors:
        href = a.get('href')
        if isinstance(href, str) and href.startswith('http'):
            links.append(href)

    # 5. Return only the first `limit` links, reversed for latest news first
    return links[:limit][::-1]

news_links = get_all_news_kudasai(base_url)

# Uncomment to debug:
# for idx, link in enumerate(news_links, start=1):
#     print(f"{idx}. {link}")