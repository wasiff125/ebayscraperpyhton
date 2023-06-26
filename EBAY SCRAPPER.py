import requests
from bs4 import BeautifulSoup
import csv


base_url = "https://www.ebay.com/sch/260018/i.html?_from=R40&_nkw=t+shirt&LH_TitleDesc=0&_ipg=240"

num_pages = 50
counter = 1

data = [] 

for page in range(1, num_pages + 1):
    url = f"{base_url}&_pgn={page}"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "lxml")

    titles = soup.find_all("div", class_="s-item__title")
    prices = soup.find_all("span", class_="s-item__price")
    image_tags = soup.find_all("img")

    for title in titles:
        title_text = title.text.strip()
        title_with_number = f"{counter}. {title_text}"
        counter += 1

        for price in prices:
            price_text = price.text.strip()

        data.append([title_with_number, price_text]) 

        print(title_with_number)
        print("PRICE: " + price_text)
        print()

# Save data to CSV file
filename = "ebay.data.csv"
with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])
    writer.writerows(data)

print(f"Scraped data saved to {filename}.")
