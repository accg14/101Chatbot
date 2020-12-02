import numpy as np, nltk
import random
from nltk.stem import WordNetLemmatizer

def clean_up_sentence(sentence):
  lemmatizer = WordNetLemmatizer()
  sentence_words = nltk.word_tokenize(sentence)
  sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
  return sentence_words

def bow(sentence, words, show_details=True):
  print(sentence)
  sanitized_sentence = clean_up_sentence(sentence)

  bag = [0]*len(words)
  for s in sanitized_sentence:
    for i,w in enumerate(words):
      if w == s:
        bag[i] = 1
        if show_details:
          print ("found in bag: %s" % w)
  return(np.array(bag))

def get_response(ints, intents_json):
  tag = ints[0]['intent']
  list_of_intents = intents_json['intents']
  for i in list_of_intents:
    if(i['tag']== tag):
      result = random.choice(i['responses'])
      break
  return result