#import nltk, numpy as np
#from nltk.stem import WordNetLemmatizer
#lemmatizer = WordNetLemmatizer()

#def sanitize(sentence):
#  sentence_words = nltk.word_tokenize(sentence)
#  sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
#  return sentence_words

#def to_bag_of_words(sentence, words):
#  sentence_words = sanitize(sentence)

#  bag = [0]*len(words)
#  for s in sentence_words:
#    for i,w in enumerate(words):
#      if w == s:
#        bag[i] = 1
#        print ("Founded in bag: %s" % w)
#    return(np.array(bag))
