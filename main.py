from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import json

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_url = "https://www.emag.ro/telefoane-mobile/c"

# opens the connection and downloads html page from url
uClient = uReq(page_url)

# parses html into a soup data structure to traverse html
# as if it were a json data type.
page_soup = soup(uClient.read(), "html.parser")
uClient.close()

# finds each product from the store page
#containers = page_soup.findAll("div", {"class": "card-item"})

containers = page_soup.findAll("button", {"class": "add-to-favorites btn btn-sm btn-default btn-icon btn-block gtm_xik37z hidden-grid"})



# loops over each product and grabs attributes about
# each product
for container in containers:
	product_info = container['data-product']
	product_info_json = json.loads(product_info)
	brand = product_info_json['product_name']
	price = product_info_json['price']
	print("Phone: " + brand)
	print("Price: " + str(price) + "\n")



