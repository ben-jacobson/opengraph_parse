from opengraph_parse import parse_page

if __name__== "__main__":
    parsed_og_tags = parse_page("http://www.facebook.com", ["og:url", "og:image", ])
    
    for key, value in parsed_og_tags.items():
        print (f"'{key}' : '{value}'")