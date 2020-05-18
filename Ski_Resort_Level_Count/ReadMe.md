# Count all trail levels of ski resorts at New England area

This project generates a simple spider by utilizing Beautifulsoup library to crawl [liftopia](https://www.liftopia.com) for counting Beginner, Intermediate, Advanced and Expert trails number of ski resort.

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
