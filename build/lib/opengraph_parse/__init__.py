from bs4 import BeautifulSoup
import requests

# By no means is this a complete list, but it is very easy to search for the ones you need later. 
KNOWN_OPENGRAPH_TAGS = [
    "og:site_name",
    "og:title",
    "og:locale",
    "og:type",
    "og:image",
    "og:url", 
    "og:image:url",
    "og:image:secure_url",
    "og:image:type",
    "og:image:width",
    "og:image:height",
    "og:image:alt",
    ]

def parse_page(page_url, tags_to_search = KNOWN_OPENGRAPH_TAGS):
    '''
    Parses a page, returns a JSON style dictionary of all OG tags found on that page. 

    Passing in tags_to_search is optional. By default it will search through KNOWN_OPENGRAPH_TAGS constant, but for the sake of efficiency, you may want to only search for 1 or 2 tags

    Returns False if page is unreadable
    '''
    # read the html from the page
    response = requests.get(page_url)

    if response.status_code is not 200:
        return False

    # set up beautiful soup
    soup = BeautifulSoup(response.content, 'html.parser')

    # loop through the known list of opengraph tags, searching for each and appending a dictionary as we go.
    found_tags = {}

    for og_tag in tags_to_search:
        new_found_tag = soup.find("meta",  property=og_tag)
        if new_found_tag is not None:
            found_tags[new_found_tag["property"]] = new_found_tag["content"]

    return found_tags
