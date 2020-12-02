import random, json, pickle, nltk
import numpy as np
from nltk.stem import WordNetLemmatizer

def load_dataset():
  lemmatizer = WordNetLemmatizer()
  nltk.download('punkt')
  nltk.download('wordnet')

  words, classes, documents = load_sources(lemmatizer)

  training = initialize_training_data(documents,lemmatizer,words,classes)

  train_x = list(training[:,0])
  train_y = list(training[:,1])
  print('training data created')
  return train_x,train_y

def initialize_training_data(documents,lemmatizer,words,classes):
  training = []
  output_empty = [0] * len(classes)

  for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]

    for w in words:
      bag.append(1) if w in pattern_words else bag.append(0) 

    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1

    training.append([bag, output_row])

  random.shuffle(training)
  training = np.array(training)
  return training

def load_sources(lemmatizer):
  words = []
  classes = []
  documents = []

  ignore_words = ['?', '!']
  data_file = open('sources/intents.json').read()
  intents = json.loads(data_file)
  
  for intent in intents['intents']:
    for pattern in intent['patterns']:
      tokenized_word = nltk.word_tokenize(pattern)
      words.extend(tokenized_word)
      documents.append((tokenized_word, intent['tag']))

      if intent['tag'] not in classes:
        classes.append(intent['tag'])

  words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
  words = sorted(list(set(words)))

  classes = sorted(list(set(classes)))

  return words, classes, documents



