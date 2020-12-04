# 101 Chatbot
# Intro
This project has been builded as fork of [HowToCreateAChatbot](https://towardsdatascience.com/how-to-create-a-chatbot-with-python-deep-learning-in-less-than-an-hour-56a063bdfc44), which a few changes (modularization).
The goal is to create a Chatbot which is capable of interact with a human beign, taking about health-related topics.

# How it works?
## 1. Training
The training step is the first of all of them. Here, the model receives training inputs and it is trained.
## 2. Sanitize input
Every time there is a new user input, it is sanitized, which consists in: lower a word to its lemma, and remove it if its a stop word.
## 3. Translate to bag of words
Once the sentence (input) has been sanitized, it is translated to bag of words, marking when a word that belongs to the bag appears.
## 4. Predict the kind of input
Use the model (already trained) to predict the type of input.
## 5. Generate (retrieve) an appropiate response
With the type of input as a key, retrieve a response which matches whit it.
# Architecture

# Model settings
  - Sequential neural network (multi-layer perceptron)
  - 3 layers (128 | 64 | #categories )
  - Activation functions: relu -> relu -> softmax
  - Optimizer: sgd
  - Loss: categorical crossentropy
 
# Tech stack
  - Python 3.6.9
  - numpy 1.19.4
  - nltk 3.5
  - tensorflow 1.14.0
  - random
  - tkinter

### How to use?
```sh
$ python3 chat_gui.py
```

# Further Work
 - Try with RNN
 - Try with other sequential configs
 - Re train over interaction
 - Resolve using word embeddings
 - Build the chatbot through some appropiate framework

License
----

MIT
