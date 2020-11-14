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
    
    
    results = soup.find(id="headword-es")
    results = remove_before_char(remove_before_char(str(results),'>'),'>')
    results=remove_after_char(results,'<')
   # results.strip(' ')
    infinitive=results
    
    return infinitive
  




def get_translation(soup):
    results = soup.find(id="dictionary-neodict-es").find('div', class_='_1IN7ttrU').find('a', class_='_1UD6CASd')#.find('td', class_='ToWrd')
    results=remove_before_char(str(results), '>')
    results=remove_after_char(str(results), '<')
   
    return results


with open('translation.csv', mode='w', newline='') as translation_file:
    translation_writer = csv.writer(translation_file)#translation_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    with open("input.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            URL = link+line+'?langFrom=es'
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')
            infinitive = get_infinitive(soup)
            translation =  get_translation(soup)
            translation_writer.writerow([translation,infinitive])

            print(infinitive)
            print(translation)
            print("")
           
print("Translation finished")









    


