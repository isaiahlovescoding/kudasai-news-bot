import requests
from bs4 import BeautifulSoup

#https://somoskudasai.com/noticias/ here you can find the news in general

base_url = 'https://somoskudasai.com/noticias/'

#You can modify the limit if you want but i think 5 news per day is good

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
    # Note: in CSS selector, colons and other special chars must be escaped with a backslash

    anchors = soup.select(selector)

    # 4. Extract the href attributes
    links = [a.get('href') for a in anchors if a.get('href')]

    # 5. Return only the first `limit` links
    return links[:limit][::-1] #I reversed the list so it starts with the latest news this is important to main.py


news_links = get_all_news_kudasai(base_url)


#if you want to see the news links and the list the function got then uncomment the next lines

# for idx, link in enumerate(news_links, start=1):
#     print(f"{idx}. {link}")
#     print(news_links)

# This MIGHT be ai slop, if you can improve it that would make you a first class coder!