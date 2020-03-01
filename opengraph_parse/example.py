import __init__ as opengraph_parse

if __name__== "__main__":
    parsed_og_tags = opengraph_parse.parse_page("http://www.facebook.com", tags_to_search=["og:title", "og:url", "og:image"], fallback_tags={'og:title': 'title'})
    
    for key, value in parsed_og_tags.items():
        print (f"'{key}' : '{value}'")