# coding: utf-8

import requests, bs4

# name, programm-link, title-selector, date-selector, get date sibling?

theaters = [
    ['Freiluftkino Rehberge', 'http://freiluftkino-rehberge.de/', '.teasertable .teaserzelle .teasertitel', '.teasertable .teaserzelle .teasertag'],
    ['Filmrauschpalast', 'http://www.filmrausch.de/', '#openair .list-group a', '#openair .list-group a strong', True],
    ['Pompeji - Freiluftkino Ostkreuz', 'https://zukunft-ostkreuz.de/freiluftkino.html', '.ui-list--movies .ui-title', '.carousel2 .carousel2__slide'],
    ['Freiluftkino Insel im Cassiopeia', 'http://www.freiluftkino-insel.de/html/program', '#program_area [itemprop="name"]', '#program_area .ProgramDate'],
    ['Freiluftkino Friedrichshain', 'http://www.freiluftkino-berlin.de/', '.teasertable .teaserzelle .teasertitel', '.teasertable .teaserzelle .teasertag'],
    ['Freiluftkino Kreuzberg', 'http://www.freiluftkino-kreuzberg.de/', '.teasertable .teaserzelle .teasertitel', '.teasertable .teaserzelle .teasertag'],
    ['Freilichtbühne am Weißensee', 'http://freilichtbuehne-weissensee.de/', '.listing h2.posttitle', '.listing .listContent .dateInfo'],
    ['Open-Air-Kino Spandau', 'http://www.openairkino-spandau.de/spielplan', '.main .panel-heading h4', '.main .panel-heading p'],
    ['Freiluftkino Hasenheide', 'http://freiluftkino-hasenheide.de/2018/index.php/programm', '.ic-list-events .event h2', '.ic-list-events .nextdate .ic-next-today']
]


for th in theaters:
    if len(th) > 2:
        res = requests.get(th[1])
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, "lxml")
        date = ""
        title = ""

        if len(soup.select(th[2])) > 0:
            title = soup.select(th[2])[0].text.strip()
            if len(th) > 4 and th[4] == True:
                title = soup.select(th[3])[0].next_sibling.strip()
        else:
            title = "error"

        if len(soup.select(th[3])) > 0:
            date = soup.select(th[3])[0].text.strip()
        else:
            date = "error"

        print(th[0] + ' ' + '\t' + title + '\t' +  date)
