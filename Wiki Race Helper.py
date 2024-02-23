#import pandas as pd
import requests
from bs4 import BeautifulSoup as stew
import win32clipboard

#main
#settings
#scrape
#output
#loop until you win
ignoreMain=True
ignoreAbout=True
ignoreCategory=True
readClipboard=False
about = """
This program reduces a wikipedia article to its links to other wikipedia articles to help you win your races. \n
By default, main, about, and category pages are ignored. This program can also read wikipedia links directly from your clipboard. \n
To change default settings or enable clipboard reading, type "settings"
To enable main pages type "set ignoreMain = False", to disable: "set ignoreMain = True"
To enable about pages type "set ignoreAbout = False", to disable: "set ignoreAbout = True"
To enable category pages type "set ignoreCategory = False", to disable: "set ignoreCategory = True"
To enable clipboard reading type "set readClipboard = False", to disable: "set readClipboard = True"
All commands are case sensitive.
"""
commands = ["set ignoreMain = False", "set ignoreMain = True", "set ignoreAbout = False", "set ignoreAbout = True",
           "set ignoreCategory = False", "set ignoreCategory = True", "set readClipboard = False", "set readClipboard = True"]

programStarted=False
print("Type \"settings\", \"help\" or paste a wikipedia link")

if(readClipboard==True):
    # get clipboard data
    win32clipboard.OpenClipboard()
    url = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

else:
    url= input()

if(url=='settings'):
    #print out the settings
    print("ignore main pages: " +str(ignoreMain))
    print("ignore about pages: " +str(ignoreAbout))
    print("ignore category pages: " +str(ignoreCategory))
    print("read clipboard: " +str(readClipboard))
    print("to change any settings, use the appropriate command. To view commands, type \'help\'")

if (url in commands):
          #do the command
    if(url == "set ignoreMain = False"):
          ignoreMain=False
    
    if(url == "set ignoreMain = True"):
          ignoreMain=True
          
    if(url == "set ignoreAbout = False"):
          ignoreAbout=False
          
    if(url == "set ignoreAbout = True"):
          ignoreAbout=True
          
    if(url == "set ignoreCategory = False"):
          ignoreCategory=False
   
    if(url == "set ignoreCategory = True"):
          ignoreCategory=True
        
    if(url == "set readClipboard = False"):
          readClipboard=False
    
    if(url == "set readClipboard = True"):
          readClipboard=True
            
if(url=='help'):
    print(about)
    url=input()
          
programStarted=True
    
    

try:
    req=requests.get(url)
    soup=stew(req.text)
    
except:
    print("an error occured")

#find all returns a list so can do list manipulation on it
#the first link on a wiki page is always the main_page which we don't need
#need a regex for /wiki/character:characters
linkList = set(soup.find_all('a'))
for link in linkList:
    #if the link starts with '/wiki/' then replace it with wikipedia.org/
    #link=str(link)
    #if (str(link[0:5])=="/wiki/"):
        #link.replace('/wiki/', 'wikipedia.org/')
    if ('/wiki/' in str(link.get('href'))):
        anya = str((link.get('href')))
        anya = anya.replace('/wiki/', 'wikipedia.org/')
        
        
        if(ignoreCategory==True and ":" in anya):
            pass
        
        elif(ignoreMain==True and anya == 'wikipedia.org/Main_Page'):
            pass
        
        elif("(identifier)" in anya):
            pass
        
        elif("foundation.wikimedia.orgwikipedia.org/" in anya):
            pass
        
        else:
            print(anya)
        
    #finally:
    #   print("program complete")

#def setIgnoreMain:
    

#def setIgnoreAbout:
          
#def setIgnoreCategory:
          
#def setReadClipboard:          
          
#Method to scrape
def scrape(url):
    print(url)
    
    