import random
import json
import pickle
from nltk.stem import WordNetLemmatizer
import numpy as np
from chat_functions import bow, get_response

from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

class Chatbot:
  def __init__(self):
    self.words = pickle.load(open('sources/words.pkl','rb'))
    self.classes = pickle.load(open('sources/classes.pkl', 'rb'))
    self.intents = json.loads(open('sources/intents.json').read())
    self.lemmatizer = WordNetLemmatizer()
    self.error_threshold = 0.25
    self.model = Sequential()

  def train_model(self,train_x,train_y):
    self.model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
    self.model.add(Dropout(0.5))
    self.model.add(Dense(64, activation='relu'))
    self.model.add(Dropout(0.5))
    self.model.add(Dense(len(train_y[0]), activation='softmax'))

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    self.model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    self.model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
    print("Model builded successfully")

  def predict_class(self,sentence):
    p = bow(sentence, self.words, show_details=False)
    res = self.model.predict(np.array([p]))[0]
    results = [[i,r] for i,r in enumerate(res) if r>self.error_threshold]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    
    for r in results:
      return_list.append({"intent": self.classes[r[0]], "probability": str(r[1])})
    return return_list

  def response(self,msg):
    ints = self.predict_class(msg)
    print(ints)
    res = get_response(ints,self.intents)
    return res