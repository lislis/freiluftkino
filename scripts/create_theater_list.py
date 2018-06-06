import requests, bs4

res = requests.get('https://www.berlin.de/kultur-und-tickets/tipps/film/freiluftkinos/')
res.raise_for_status()

theaterSoup = bs4.BeautifulSoup(res.text)

list = theaterSoup.select('.linklist li a')

oaTheaters = open('oa_teaters.csv', 'a')

for l in list:
    oaTheaters.write(l.text)
    oaTheaters.write(',')
    oaTheaters.write(l.get('href'))
    oaTheaters.write(',\n')

oaTheaters.close()
