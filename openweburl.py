import webbrowser

def open_website(url):
    """
    Opens a website in the default web browser.
    
    :param url: The URL of the website to open.
    """
    if webbrowser.open(url):
        print(f"Website '{url}' opened in the default web browser.")
    else:
        print(f"Error: Unable to open the website '{url}'.")

# Example usage
website_url = "https://www.google.com"
open_website(website_url)
