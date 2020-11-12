# This is a sample Python script.
from bs4 import BeautifulSoup
import requests
link = 'https://www.wordreference.com/es/en/translation.asp?spen='
old_word = input("What is the word? : ")

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

def get_infinitive(word):
    
    URL = link+word
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="articleHead").find('div', class_='inflectionsSection').find('div', attrs={'style': 'padding-left:0px; cursor:pointer;', 'onclick':'redirectWR(event,"WResen")'}).find('dl', attrs={'style':'margin:12px 0px 6px;'}).find('dt')
    results = remove_before_char(remove_before_char(remove_before_char(str(results),'>'),'>'),'>')
    results=remove_after_char(results,'<')
    results.strip(' ')
    infinitive=results
    
    return infinitive
  
def get_if_verb(word):
    # i = infinitive
    # n = not verb
    # v = verb
    word = word.strip(' ')
    #if word ends with r then infinitive verb
    if (word[-1]=='r'):
        return 'i'
    try: 
        v = get_infinitive(word)
    except Exception as e: 
        return 'n'
    return 'v'
    





def get_translation(word, isVerb):

    URL = link+word
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id="articleWRD").find('table', class_='WRD').find('tr', class_='even').find('td', class_='ToWrd')
    results=remove_before_char(str(results), '>')
    results=remove_after_char(str(results), '<')
    results=results.strip(' ')
    if isVerb: results = "to " + results
    return results





wordType = get_if_verb(old_word)
# i = infinitive
# n = not verb
# v = verb
if (wordType=='v'):
    infinitive = get_infinitive(old_word)
    print(infinitive)
    translation = get_translation(infinitive, True)
    print(translation)
if (wordType=='i'):
    translation = get_translation(old_word, True)
    print(old_word)
    print(translation)
if (wordType=='n'):
    translation = get_translation(old_word, False)
    print(old_word)
    print(translation)






    


