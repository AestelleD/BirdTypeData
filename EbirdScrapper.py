import requests
import json
from bs4 import BeautifulSoup
import datetime

url = input("https://ebird.org/hotspot/L737447?yr=all&m=&rank=hc")
urllist = url.split()
filname = input("data")
nesteddict=[]
for i in urllist:
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup.prettify())
    x = 0
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
            observe = (i.find(class_ = "Observation-meta-observer-label"))
            observe =(observe.contents[0])
            observe = observe.strip()
            birddata = (birddata.find("span"))
            birddat =(birddata.contents[0])
            birddata =(birddata.contents[0])
            format = '%d %m %Y'
            birddata = birddata.replace("Jan","1")
            birddata = birddata.replace("Feb","2")
            birddata = birddata.replace("Mar","3")
            birddata = birddata.replace("Apr","4")
            birddata = birddata.replace("May","5")
            birddata = birddata.replace("Jun","6")
            birddata = birddata.replace("Jul","7")
            birddata = birddata.replace("Aug","8")
            birddata = birddata.replace("Sep","9")
            birddata = birddata.replace("Oct","10")
            birddata = birddata.replace("Nov","11")
            birddata = birddata.replace("Dec","12")
            
            birddate = datetime.datetime.strptime(birddata, format)
         #   birddate = str(birddate)
          #  print (birddate)
            montoday = (30 * birddate.month) - 30
            birddate = int(birddate.day) + int(montoday)
            #print(birddata)
            adict = {"name":birdname,"date":birddate, "count":nob, "date2":birddat, "Observer":observe}
            nesteddict.append(adict)
            print(birdname,birddate,nob)

jsonString = json.dumps(nesteddict, indent=4)
jsonFile = open((filname + ".json"), "w")
jsonFile.write(jsonString)
jsonFile.close()


    
