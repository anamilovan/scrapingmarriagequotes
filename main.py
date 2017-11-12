from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen
import random

url = "http://quotes.yourdictionary.com/theme/marriage/"
response = urlopen(url).read()
soup = BeautifulSoup(response)

quotes = soup.findAll("p", attrs={"class": "quoteContent"})

i = 0

quote = random.sample(quotes, 5)

for qu in quote:
    i += 1
    print qu.text

