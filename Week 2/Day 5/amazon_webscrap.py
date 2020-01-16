import requests
import html5lib
from bs4 import BeautifulSoup
import time
#While True:#wrap the whole thing around and then..go

amazon_url = "https://www.amazon.com/Portable-External-Storage-Compatible-Desktop/dp/B07DKCNBGH/ref=sr_1_1_sspa?crid=I296O463PGM4&keywords=external+hard+drive&qid=1578882670&refinements=p_72%3A2661618011&rnid=2661617011&sprefix=exter%2Caps%2C524&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUlNNNzBON1pKTDhIJmVuY3J5cHRlZElkPUEwNjM1Nzk2Nk5GVDZVMUlWRFdCJmVuY3J5cHRlZEFkSWQ9QTA4OTI2NjAxMVYwSkhUTUQ2Tlo2JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
#dictionary has this 
#'key' : 'value'

agent_header = {
	"User-Agent" : agent
}
amazon_page = requests.get(amazon_url, headers=agent_header)
#print(type(amazon_page))
soup = BeautifulSoup(amazon_page.content, "html5lib")

#print(soup.prettify())#duck says meow~ 
#specific id in the soup
price_span = str(soup.find(id="priceblock_saleprice")) #converts into a str type instead of soup type
#print(price_span)

price = ""
for char in price_span:
	#assume price in usd
	#	if char == "1":
	#		price += char
	#	elif char == "2":
	#		price += char
	#this is the long way of doing searching
	#if it's a digit, = 0-9
	if char.isdigit() is True:
		price += char #adds to end of string
	if char == ".":
		price += char

print(price)
price = float(price)
max_price = 15
if price <= max_price:
	print(f"Buy now!")
else: 
	print(f"Too expensive! Get a job! >..<''")


#time.sleep(86400) #one day