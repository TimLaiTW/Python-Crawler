# Count all trail levels of ski resorts at New England area

This [project](https://github.com/TimLaiTW/Python-Crawler/blob/master/Ski_Resort_Level_Count/ski_resort_trail_data.py) generates a simple spider by utilizing Beautifulsoup library to crawl [liftopia](https://www.liftopia.com) for counting Beginner, Intermediate, Advanced and Expert trails number of ski resort. [The result shows here](https://github.com/TimLaiTW/Python-Crawler/blob/master/Ski_Resort_Level_Count/Ski_Resort_Trail_Data.text).

Get the Beautifulsoup object which represents the website as a data structure
```
nl_response = rq.get(next_link)
soup = BeautifulSoup(nl_response.text, 'html.parser')
```

Select:
```
if soup.select('h1') != []:
```

Find/FindAll:
```
for trail_category in soup.findAll('div', {'class':'small-3 columns'}):
```
