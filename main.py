# This is a sample Python script.
from bs4 import BeautifulSoup
import requests
link = 'https://www.wordreference.com/es/en/translation.asp?spen='
old_verb = input("What is the verb? : ")
infinitive = None
def remove_before_char(s,c):
    #inputs a char to remove before (c, inclusive) on a string(s)
    final = ''
    write = False
    for l in s:
        if (write==True):
            final = final +l
        if l==c:
            write = True
    return final
def remove_after_char(s,c):
    #inputs a char to remove before (c, inclusive) on a string(s)
    final = ''
    write = True
    for l in s:
        if l==c:
            write = False
        if (write==True):
            final = final +l
    return final    
        
def get_infinitive():
    global infinitive
    verb = old_verb
    URL = link+verb
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="articleHead").find('div', class_='inflectionsSection').find('div', attrs={'style': 'padding-left:0px; cursor:pointer;', 'onclick':'redirectWR(event,"WResen")'}).find('dl', attrs={'style':'margin:12px 0px 6px;'}).find('dt')
    results = remove_before_char(remove_before_char(remove_before_char(str(results),'>'),'>'),'>')
    results=remove_after_char(results,'<')
    results.strip(' ')
    infinitive=results
    return infinitive
  

def get_translation():

    if (infinitive==None):
        return print('infinitive = null')
    URL = link+infinitive
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="articleWRD").find('table', class_='WRD').find('tr', class_='even').find('td', class_='ToWrd')
    results=remove_before_char(str(results), '>')
    results=remove_after_char(str(results), '<')
    results=results.strip(' ')
    results = "to " + results
    return results





print(get_infinitive())
print(get_translation())




    


