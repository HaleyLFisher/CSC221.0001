import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://en.wikipedia.org/wiki/List_of_American_films_of_2011"
page = urlopen(url)

bs = BeautifulSoup(page.read(), "html.parser")
all_sortable_tables = bs.find_all("table", class_="wikitable")
table = all_sortable_tables[0]

A = []
B = []
C = []
D = []

for row in table.find_all("tr")[1:]:  
    cells = row.find_all(["th", "td"])
    if len(cells) >= 4:  
        A.append(cells[0].get_text().strip())  
        B.append(cells[1].get_text().strip())  
        C.append(cells[2].get_text().strip())  
        D.append(cells[3].get_text().strip())  

df = pd.DataFrame({'Rank': A, 'Title': B, 'Distributor': C, 'Domestic Gross': D})
print(df)
df.to_csv("Top_Grossing_2011_films.csv")
print("Top Grossing 2011 films created")