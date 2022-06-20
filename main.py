from nltk.corpus import stopwords
import elasticsearch
import nltk
import os
import pprint
import inflect

stopwords = set(stopwords.words('english'))
p = inflect.engine()


def searching(search):  # Chicken egg
    junk_words = ['cut', 'potato']
    removetable = str.maketrans('', '', "\\@<>%=*/ï¿½.&#$^+-?1234567890")
    phrase = search.translate(removetable)
    word_list = phrase.split()

    # with open(r"E:\slurrp cleaning\junk.csv", "r", newline="", encoding='utf8') as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         junk_words.append(row)

    singular_word_list = []
    for word in word_list:
        try:
            word_flag = p.singular_noun(word)
            if word_flag:
                word = word_flag
        except:
            pass
        singular_word_list.append(word)

    filtered_stop_words = [word for word in singular_word_list if word not in stopwords]
    final_filtered = [word for word in filtered_stop_words if word not in junk_words]
    final_filtered_phrase = ' '.join(final_filtered)
    return final_filtered_phrase



print(searching("@potato which are much #more cut cleaner than beef chicken"))
