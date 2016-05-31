from bs4 import BeautifulSoup
import urllib
r = urllib.urlopen("http://www.imdb.com/showtimes/location/US/94112").read()
soup = BeautifulSoup(r)

movieDiv = soup.find_all("div", class_="lister-item")

print len(movieDiv)

movies ={}

# print(movieDiv.div.span['data-value'])


i = 0
for element in movieDiv:
	#collect div hidden, capture all span
	temp = element.div.find_all("span")

	#print out span[1] which is name of movie
	print(i, temp[1]['data-value'].encode('utf-8'))
	i+=1

#problem missing 15 movies from list. total movies on site is 56,
#only scrapped 41 movie div


