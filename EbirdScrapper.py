import requests
import json
from bs4 import BeautifulSoup
url = input("Input Ebird.org Url")
filname = input("Input filename for .json output file")
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
x = 0
nesteddict=[]
for x in range(0,200):
    for i in soup.find_all(id="has-det-" + str(x)):
        nob = (i.find( class_ = "Observation-meta-count-label Color-text-neutral-4" ))
        nob =(nob.contents[0])
        nob = nob.strip()
        #print(nob)
        birdname = (i.find( class_ = "Heading-main" ))
        birdname =(birdname.contents[0])
        birdname = birdname.strip()
        #print(birdname)
        birddata = (i.find(class_ = "Observation-meta-date-label"))
        birddata = (birddata.find("span"))
        birddata =(birddata.contents[0])
        #print(birddata)
        adict = {"name":birdname,"date":birddata, "count":nob}
        nesteddict.append(adict)
        print(birdname,birddata,nob)

jsonString = json.dumps(nesteddict, indent=4)
jsonFile = open((filname + ".json"), "w")
jsonFile.write(jsonString)
jsonFile.close()


    
