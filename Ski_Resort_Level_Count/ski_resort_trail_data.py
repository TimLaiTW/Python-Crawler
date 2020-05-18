import requests as rq
from bs4 import BeautifulSoup
import io
import time

def resort_url(resort_name):        #resort url
    return "https://www.liftopia.com" + str(resort_name)

tStart = time.time()    #Start the timer
fp = io.open("Ski_Resort_Trail_Data.text", 'w',encoding = 'utf-8')

next_link = "https://www.liftopia.com/region/new-england"
nl_response = rq.get(next_link)
soup = BeautifulSoup(nl_response.text, 'html.parser')
for url in soup.findAll('a', {'class':'header--4 resort-row__resort-link'}):
    resort_link = rq.get(resort_url(url.get('href')))
    soup = BeautifulSoup(resort_link.text, 'html.parser')
    if soup.select('h1') != []:
        resort_name = soup.select('h1', {'class':'resort-hero-area__header__name header--1'})[0].text
        print(resort_name)
        fp.write('---' + resort_name + '---' + '\n')
        for trail_category in soup.findAll('div', {'class':'small-3 columns'}):
            trail_category_title = trail_category.find('p')
            trail_category_total = trail_category.find('span')
            trail_info = ': '.join([trail_category_title.string, trail_category_total.string])
            fp.write(trail_info + '\n')

tEnd = time.time()      #Stop the timer
fp.close()
print("It cost %f sec" % (tEnd - tStart))
