# coding: utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import json

today = datetime.datetime.now().strftime('%d.%m.%Y')
today_find = datetime.datetime.now().strftime('%d.')

screeningFile = open('data/screenings_'+today+'.csv', 'w')

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", chrome_options=options)

theaters = [
    ['Freiluftkino Rehberge', 'http://freiluftkino-rehberge.de/', '.teasertable .teaserzelle .teasertitel', '.teasertable .teaserzelle .teasertag'],
    ['Filmrauschpalast OpenAir', 'http://www.filmrausch.de/', '#openair .list-group a', '#openair .list-group a:contains(\''+ today_find +'\')', True],
    ['Pompeji - Freiluftkino Ostkreuz', 'https://www.kinoheld.de/kino-berlin/freiluftkino-pompeji-open-air-am-ostkreuz-berlin/shows/movies?mode=widget&cid=MjYwOTQzNg&layout=movies&rb=0&design=kinos-am-ostkreuz', '.movie__title.u-mb-3', '.carousel2 .carousel2__slide'],
    ['Freiluftkino Insel im Cassiopeia', 'http://www.freiluftkino-insel.de/html/program', '#program_area [itemprop="name"]', '#program_area .ProgramDate'],
    ['Freiluftkino Friedrichshain', 'http://www.freiluftkino-berlin.de/eine_woche.php', '.teasertable .teaserzelle .teasertitel', '.teaserzelle .teaserdatum'],
    ['Freiluftkino Kreuzberg', 'http://www.freiluftkino-kreuzberg.de/', '.teasertable .teaserzelle .teasertitel', '.teasertable .teaserzelle .teasertag'],
    ['Freilichtbühne am Weißensee', 'http://freilichtbuehne-weissensee.de/', '.posttitle', '.dateInfo:contains(\''+ today_find +'\')'],
    ['Open-Air-Kino Spandau', 'http://www.openairkino-spandau.de/spielplan', '.main .panel-heading h4', '.main .panel-heading p:contains(\''+ today_find +'\')'],
    ['Freiluftkino Hasenheide', 'http://freiluftkino-hasenheide.de/2018/index.php/programm', '.ic-list-events .event h2', '.ic-list-events .nextdate .ic-next-today']
]

collection = []

for th in theaters:
    if len(th) > 3:
        title = ''
        date = ''
        browser.get(th[1])
        try:
            title = browser.find_element_by_css_selector(th[2]).text.strip()
        except:
            title = ''

        try:
            date = browser.find_element_by_css_selector(th[3]).text.strip()
        except:
            date = ''
            title = ''

        # Filmrauschpalast is tricky
        if len(th) == 5 and th[4] == True:
            try:
                date = browser.find_element_by_css_selector(th[3]).text.strip()
                title = ''
            except:
                title = ''
                date = ''

        # relevant for Pompeji
        date = date.replace('heute', today)
        date = date.replace('\n', ' ')

        if title != '':
            screeningFile.write(th[0] + ',' + title + ','+ date + ','+ th[1]+'\n')
            collection.append({'cinema': th[0], 'title': title, 'date': date, 'link': th[1]})

        print(th[0] + '...')

screeningFile.close()
browser.close()

with open('screenings.json', 'w') as outfile:
    json.dump(collection, outfile)

print('Done!')
