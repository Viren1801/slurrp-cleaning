import nltk
import csv
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stopwords = set(stopwords.words('english'))

nltk.download('stopwords')
nltk.download('punkt')

list2 = []

with open(r"E:\slurrp cleaning\ingredient_6L.csv", "r", newline="", encoding='utf8') as file:
    reader = csv.reader(file)
    for row in reader:
        list2.append(row)

# removing the address that stored in the list
result = [i[1:] for i in list2]
#print(result)
# converting the list from 2d to 1d
final_result = [j for sub in result for j in sub]
#print(final_result)


# removing the stop words from the list
removed_stop_words = []
for sentence in final_result:
    temp_list = []
    for word in sentence.split():
        if word not in stopwords:
            temp_list.append(word.lower())
    removed_stop_words.append(' '.join(temp_list))
#print(removed_stop_words)
# removing the other special character from the dataset

removetable = str.maketrans('', '', '\\@<>`~!_%=*/ï¿½.&#$^+-?1234567890')
removed_special_characters = [s.translate(removetable) for s in removed_stop_words]
#print(removed_special_characters)

# removed the content of the brackets and brackets itself
removed_brackets = []
for i in removed_special_characters:
    removed_brackets.append(re.sub("\(.*?\)"," ", i))
# print(removed_brackets)

removed_brackets_curly = []
for i in removed_brackets:
    removed_brackets_curly.append(re.sub("\{.*?\}"," ", i))

removed_brackets_complete = []
for i in removed_brackets_curly:
    removed_brackets_complete.append(re.sub("\[.*?\]","", i))
# print(removed_brackets_complete)

for i in ['(', ')', '{', '}', '[', ']']:
    removed_brackets_complete = [sub.replace(i, '') for sub in removed_brackets_complete]
#print(removed_brackets_complete)
# removing the units in the dataset


list_not_needed = ['â\\x81\\x84','tspn', '–', 'g', 'Can', 'INGREDIENTS', 'For', 'Mm', 'ml', 'cm', 'm', 'l', 'mm', 'kg', 'gm', 'diameter', 'lengthways', 'widthways', 'quartered', 'quater', 'quantity', 'Milliliters', 'teaspoons', 'cut', 'divide', 'knife', 'upside', 'topside','downside', 'corner','skin','removed','remove','peeled','peel','pieces','joints','hours','minute','seconds','second','mixed' ,'ahead','Note','day','ahead','broke','break','broken','serve','lengths','F','sliced','inch','inches','x','crossways','chooped','chop','across','Quantity','Note:','halved','split','cleaned','To','serve','plate','cmxcm','Xcm','xcm','Lcm','intocm', 'Each', 'Extra', 'each', 'extra', 'plus', 'trimmed', 'serve:', 'chopped', 'best','serving','the','made','dressing', 'Mixed', 'rinsed', 'drained','tsp','finely','tbsp','crushed','finely','grated','cup','Home']
removed_unnecessary = []
for sentence in removed_brackets_complete:
    temp_list = []
    for word in sentence.split():
        if word not in list_not_needed:
            temp_list.append(word)
        else:
            word.replace(word, '')
    removed_unnecessary.append(' '.join(temp_list))

#print(removed_unnecessary)

removed_unnecessary_commas = []
for sentence in removed_unnecessary:
    sentence = sentence.replace(',', ' ')
    removed_unnecessary_commas.append(sentence)

#print(removed_unnecessary_commas)

removed_collon = []
for sentence in removed_unnecessary_commas:
    sentence = sentence.replace(':', ' ')
    removed_collon.append(sentence)

#print(removed_collon)

removed_semicollon = []
for sentence in removed_collon:
    sentence = sentence.replace(';', ' ')
    removed_semicollon.append(sentence)

#print(removed_semicollon)


unique = set(removed_semicollon)
list_unique = list(unique)


import csv
with open(r'E:\slurrp cleaning\unique_search_ingredients.csv', 'w', newline='', encoding='utf8') as csvfile:
    writer = csv.writer(csvfile)
    for i in list_unique:
        writer.writerows([[i]])


