# opengraph_parse
Ben Jacobson 2020

Parses Open Graph meta tags of web pages. Use this to generate previews of web pages.

The purpose of this is to make it easy to scrape a pages opengraph meta tags. This is helpful if you ever want to create a preview of a web page like you'd see when you post to social media, or post a link on Slack. 

Uses Python >=3.6.9

# Installation
pip install opengraph_parse

# Usage

from opengraph_parse import parse_page

if __name__== "__main__":
    # parse the page
    parsed_og_tags = parse_page("http://www.facebook.com", ["og:url", "og:image", ])
    
    # result is a python dict containing the opengraph tags, simply print them out, or use a for loop to iterate over these. 
    for key, value in parsed_og_tags.items():
        print (f"'{key}' : '{value}'")