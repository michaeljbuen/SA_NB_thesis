from process import df
from textblob import TextBlob,Word
from textblob.classifiers import NaiveBayesClassifier

import nltk
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier as nbc
from nltk.tokenize import word_tokenize
from itertools import chain

import random
import time

tr = list()

def run_nb(id):
    id = id
    start = time.time()
    rawtext = df['content'][id - 1]
    # NLP Stuff
    blob = TextBlob(rawtext)
    received_text2 = blob
    # blob_sentiment, blob_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
    number_of_tokens = len(list(blob.words))

    stop = list()
    slist = list()
    for word in blob.words:

        if word not in stopwords.words('english'):
            stop.append(word)
            slist.append(word)
        else:
            stop.append('\u0336'.join(word) + '\u0336')

    markstop = ' '.join(stop)

    # slist = (word for word in blob.words if word not in stopwords.words('english'))

    new_text = ' '.join(slist)

    new_blob = TextBlob(new_text)
    new_received = new_blob

    blob_sentiment, blob_subjectivity = new_blob.sentiment.polarity, new_blob.sentiment.subjectivity
    # Extracting Main Points

    nouns = []
    # pos = []
    # neg = []
    # ntr = []

    train = [
        ('I love this sandwich.', 'pos'),
        ('This is an amazing place!', 'pos'),
        ('I feel very good about these beers.', 'pos'),
        ('This is my best work.', 'pos'),
        ("What an awesome view", 'pos'),
        ('I do not like this restaurant', 'neg'),
        ('I am tired of this stuff.', 'neg'),
        ("I can't deal with this", 'neg'),
        ('He is my sworn enemy!', 'neg'),
        ('My boss is horrible.', 'neg')
    ]

    if blob_sentiment > 0.0:
        # pos.append([format_sentence(str(new_received)), 'pos']
        tr.append((str(new_received), 'pos'))

    elif blob_sentiment < 0.0:
        # neg.append([format_sentence(str(new_received)), 'neg'])
        tr.append((str(new_received), 'neg'))
    else:
        # ntr.append([format_sentence(str(new_received)), 'ntr'])
        tr.append((str(new_received), 'ntr'))

    # print(blob_sentiment)

    # all_words = set(word.lower() for passage in tr for word in word_tokenize(passage[0]))
    # t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in tr]

    # training = pos[:int((.8) * len(pos))] + neg[:int((.8) * len(neg))]
    # test = pos[int((.8) * len(pos)):] + neg[int((.8) * len(neg)):]

    print(tr)

    vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in tr]))

    feature_set = [({i: (i in word_tokenize(sentence.lower())) for i in vocabulary}, tag) for sentence, tag in
                   tr]

    classifier = nbc.train(feature_set)

    test_sentence = "This is the worst band I've ever heard!"
    featurized_test_sentence = {i: (i in word_tokenize(test_sentence.lower())) for i in vocabulary}

    print("test_sent:", test_sentence)
    print("tag:", classifier.classify(featurized_test_sentence))
    classifier.show_most_informative_features()

def process(id):
    #run_nb(id)
    id=id
    start = time.time()
    rawtext = df['content'][id-1]
        # NLP Stuff
    blob = TextBlob(rawtext)
    received_text2 = blob
    #blob_sentiment, blob_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
    number_of_tokens = len(list(blob.words))

    stop=list()
    slist=list()
    for word in blob.words:

        if word not in stopwords.words('english'):
            stop.append(word)
            slist.append(word)
        else:
            stop.append('\u0336'.join(word) + '\u0336')

    markstop = ' '.join(stop)

    #slist = (word for word in blob.words if word not in stopwords.words('english'))

    new_text = ' '.join(slist)

    new_blob = TextBlob(new_text)
    new_received = new_blob

    blob_sentiment, blob_subjectivity = new_blob.sentiment.polarity, new_blob.sentiment.subjectivity
    #     # Extracting Main Points
    #
    nouns = []
    # # pos = []
    # # neg = []
    # # ntr = []




        # print(train)
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
             final_time = time.time()- start
             len_of_words=0

        # classifier = NaiveBayesClassifier.train(t)
        #
        # classifier.show_most_informative_features()

    #return (received_text2, new_received, number_of_tokens, blob_sentiment, blob_subjectivity, summary, final_time, len_of_words, pos, neg, training, test)
    return (received_text2, new_received, number_of_tokens, blob_sentiment, blob_subjectivity, summary, final_time, len_of_words, markstop)


def format_sentence(sent):
    return({word: True for word in nltk.word_tokenize(sent)})



