import requests
from bs4 import BeautifulSoup
import json


result_dict = dict()

url = 'https://www.amazon.in/s?k=books'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}

try:
    webpage = requests.get(url, headers=headers)
    # print(webpage)
    webpage.raise_for_status()  # Raise an exception for HTTP errors
    soup = BeautifulSoup(webpage.content, 'html.parser')

    links = soup.find_all("a", attrs={
        'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

    for i, one_link in enumerate(links):

        link = one_link.get('href')

        if (link.startswith('https')):
            product_item = link
        else:
            product_item = "https://amazon.in" + link

        inner_webpage = requests.get(product_item, headers=headers)
        inner_webpage.raise_for_status()
        new_soup = BeautifulSoup(inner_webpage.content, 'html.parser')

        result = "Product title not available"
        price = "Price not available"

    # Find the title and price elements
        title_element = new_soup.find(
            'span', attrs={'class': 'a-size-extra-large celwidget'})
        price_element = new_soup.find('span', attrs={'id': 'price'})

        # If title element is found, extract the text
        if title_element:
            result = title_element.get_text(strip=True)

        # If price element is found, extract the text and remove currency symbol
        if price_element:
            price = price_element.get_text(
                strip=True).replace('₹', '').replace(',', '')

        result_dict[i+1] = {
            "price": price,
            "title":  result
        }

        print(price, result)
        if (i >= 10):
            break

    else:
        print("No product links found.")

    with open("results.json", "w") as obj:
        print("hello")
        obj.write(json.dumps(result_dict, indent=4))

except requests.exceptions.RequestException as e:
    print("An error occurred:", e)
except Exception as ex:
    print("An error occurred:", ex)
