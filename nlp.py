from process import df
from textblob import TextBlob,Word

import nltk
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier

import random
import time

def process(id):
    id=id
    start = time.time()
    rawtext = df['content'][id-1]
        # NLP Stuff
    blob = TextBlob(rawtext)
    received_text2 = blob
    #blob_sentiment, blob_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
    number_of_tokens = len(list(blob.words))

    slist = (word for word in blob.words if word not in stopwords.words('english'))
    new_text = ' '.join(slist)
    new_blob = TextBlob(new_text)
    new_received = new_blob

    blob_sentiment, blob_subjectivity = new_blob.sentiment.polarity, new_blob.sentiment.subjectivity
        # Extracting Main Points
    nouns = list()

    # pos = []
    # neg = []
    # ntr = []
    # if blob_sentiment > 0.0:
    #     pos.append([format_sentence(str(new_received)), 'pos'])
    #
    # elif blob_sentiment < 0.0:
    #     neg.append([format_sentence(str(new_received)), 'neg'])
    #
    # else:
    #     ntr.append([format_sentence(str(new_received)), 'ntr'])
    #     print(blob_sentiment)

    # training = pos[:int((.8) * len(pos))] + neg[:int((.8) * len(neg))]
    # test = pos[int((.8) * len(pos)):] + neg[int((.8) * len(neg)):]

    for word, tag in new_blob.tags:
         if tag == 'NN':
            nouns.append(word.lemmatize())
            len_of_words = len(nouns)
            rand_words = random.sample(nouns, len(nouns))
            final_word = list()
            for item in rand_words:
                word = Word(item).pluralize()
                final_word.append(word)
                summary = final_word
                end = time.time()
                final_time = end - start
         else:
             summary = ''
             final_time = time.time()-start
             len_of_words=0

    #classifier = NaiveBayesClassifier.train(training)
    #classifier.show_most_informative_features()

    #return (received_text2, new_received, number_of_tokens, blob_sentiment, blob_subjectivity, summary, final_time, len_of_words, pos, neg, training, test)
    return (received_text2, new_received, number_of_tokens, blob_sentiment, blob_subjectivity, summary, final_time, len_of_words)


def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})






# next, split labeled data into the training and test data
