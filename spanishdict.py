from os import error
from bs4 import BeautifulSoup
import requests
link = 'https://www.spanishdict.com/translate/'
import csv

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

def get_infinitive(soup):
    
    try:
        results = soup.find(id="headword-es")
        results = remove_before_char(remove_before_char(str(results),'>'),'>')
        results=remove_after_char(results,'<')
    # results.strip(' ')
    except error as e:
        print(e)
        return None
    infinitive=results
    
    return infinitive
  




def get_translation(soup):
    try:
        results = soup.find(id="dictionary-neodict-es").find('div', class_='_1IN7ttrU').find('a', class_='_1UD6CASd')#.find('td', class_='ToWrd')
        results=remove_before_char(str(results), '>')
        results=remove_after_char(str(results), '<')
    except error as e:
        print (e)
        return None
    return results







with open('translation.csv', encoding='UTF-8',mode='w', newline='') as translation_file:
    translation_writer = csv.writer(translation_file)
    with open('input.txt', encoding='UTF-8', mode='r', newline='') as input:
        for w in input:
                try: 
                    stripped_line = w.strip()
                    URL = link+w+'?langFrom=es'
                    page = requests.get(URL)
                    soup = BeautifulSoup(page.content, 'html.parser')
                    spanish_word = get_infinitive(soup)
                    translation =  get_translation(soup)
                    toWrite = True
                except error as e:
                    print(e)
                with open('all_translations.txt', mode='r', newline='') as all_translations_file:
                    for l in all_translations_file:
                        if l.strip() == spanish_word.strip():
                            toWrite=False
                if toWrite and spanish_word != None and translation != None:                   
                    translation_writer.writerow([translation,spanish_word])
                    with open('all_translations.txt', encoding='UTF-8', mode='a', newline='') as all_translations_file:
                         all_translations_file.write('\n'+spanish_word)
                    print(spanish_word)
                    print(translation)
                    print("")
                else: print("already translated")


print("Translation finished")









    


