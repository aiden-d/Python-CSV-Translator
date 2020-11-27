#test
from os import error
from bs4 import BeautifulSoup
import requests
link = 'https://www.spanishdict.com/translate/'
import csv
import sys
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
        results = str(soup.find(id="quickdef1-es"))
        results = remove_before_char(results,'>')
        results = remove_before_char(results,'>')
        results = remove_after_char(results,'<')
        try: 
            results2 = str(soup.find(id="quickdef2-es"))
            results2 = remove_before_char(results2,'>')
            results2 = remove_before_char(results2,'>')
            results2 = remove_after_char(results2,'<')
        except error as e:
            print(e)
        print("")
    except error as e:
        print(e)
        return None
    
    if results2 != '':
        return results+ " or " + results2
    else: return results


def single(i):
    try: 
        stripped_line = i.strip()
        URL = link+i+'?langFrom=es'
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        spanish_word = get_infinitive(soup)
        translation =  get_translation(soup)
        print(translation)
    except error as e:
        print(e)

def batch():
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

cont = True
while cont:
    i = input("Batch (b), quit (q) or word: ")
    if i == 'q':
        sys.exit()
    else:
        if i=='b': batch()
        else: single(i)
print("Translation finished")








    


