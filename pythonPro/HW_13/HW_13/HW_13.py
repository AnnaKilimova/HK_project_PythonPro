import requests as r
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
from typing import Optional, List, Dict


# Function to load the HTML content of a page
def get_page(url: str) -> Optional[BeautifulSoup]:
    """
    Downloads HTML content of a page.

    Args:
        url (str): The URL of the page to download.

    Returns:
        Optional[BeautifulSoup]: Parsed HTML content if the request is successful,
        otherwise None.
    """
    try:
        response = r.get(url)
        response.raise_for_status()  # Check the status of the response
        return BeautifulSoup(response.text, 'html.parser')
    except r.RequestException as e:
        print(f"Error loading page: {e}")
        return None


# Function to parse news items from a page
def parse_news(soup: BeautifulSoup) -> List[Dict[str, str]]:
    """
    Parses news items from the HTML content.

    Args:
        soup (BeautifulSoup): Parsed HTML content.

    Returns:
        List[Dict[str, str]]: A list of dictionaries, each containing information about a news item.
    """
    fields = []

    try:
        # Locate all news item elements; replace 'archiveCard' with the actual news block class/tag on your site
        content = soup.find_all('article', class_='archiveCard')
        if not content:
            print("Error: No news items found.")
            return fields

        for i in content:
            # Extract and validate publication date
            date_tag = i.find('span', class_="c-teaser__date")
            date = date_tag.contents[0].strip() if date_tag else "Date not available"

            # Extract and validate title and link
            title_tag = i.find('h3', class_='archiveCard__title').find('a')
            if title_tag:
                title = title_tag.text.strip()
                link = title_tag['href'].strip()
            else:
                title = "Title not available"
                link = "Link not available"

            # Extract short description
            description_tag = i.find('div', class_='archiveCard__description small')
            description = description_tag.text.strip() if description_tag else "Description not available"

            fields.append({
                'Publication Date': date,
                'News Title': title,
                'Link': link,
                'Short Description': description
            })

    except AttributeError as e:
        print(f"HTML parsing error: {e}")

    return fields


# Function to save news items to a CSV file
def save_to_csv(data: List[Dict[str, str]], filename: str = 'news.csv') -> None:
    """
    Saves news data to a CSV file.

    Args:
        data (List[Dict[str, str]]): List of dictionaries containing news data.
        filename (str): Name of the CSV file to save data to. Default is 'news.csv'.
    """
    if not data:
        print("No data to save.")
        return

    df = pd.DataFrame(data)
    try:
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Data saved to file {filename}")
    except IOError as e:
        print(f"Error saving to CSV file: {e}")


# Main function to start parsing process
def main(url: str, days: int = 7) -> None:
    """
    Main function to load, parse, and save news data.

    Args:
        url (str): The URL of the news page to parse.
        days (int): Number of days for filtering recent news items.
    """
    soup = get_page(url)
    if soup:
        news_data = parse_news(soup)
        save_to_csv(news_data)  # Call function to save data
    else:
        print("Failed to load page.")


# Run the script with the target news URL
if __name__ == "__main__":
    news_url = 'https://kyivindependent.com/'  # Replace with the URL of the news page
    main(news_url)
