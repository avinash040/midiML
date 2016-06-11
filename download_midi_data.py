"""
    Download and save the midi data from the following sites:
        - www.piano-midi.de/midi_files.htm

"""
url1 = "http://www.piano-midi.de/midi_files.htm"
base_url1 = "http://www.piano-midi.de/"

from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import re, shutil, requests, os

save_loc =  os.path.abspath("/Users/avinashvarma/PycharmProjects/midiML")

response = urlopen(url1)
html = response.read()
soup = BeautifulSoup(html, "lxml")

composers_table = soup.find("table", {"class":"midi"})

composers_link = []
for row in composers_table.findAll('tr'):
    col = row.findAll('td')[:1]
    if (len(col) > 0 ):
        link = re.findall('href=\".*\"',str(col[0]))
        composers_link.append(base_url1+link[0].strip('href=\"'))

print(composers_link)

for link in composers_link:
    print(link)
    #file = requests.get(link, stream=True)






