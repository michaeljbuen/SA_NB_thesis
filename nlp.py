from process import df, rf
from textblob import TextBlob,Word
from textblob.classifiers import NaiveBayesClassifier

import nltk
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier as nbc
from nltk.tokenize import word_tokenize
from itertools import chain

import random
import time
import json

tr = list()
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

t_rf = list()
def run_nb(id):
    id = id
    start = time.time()
    rawtext = df['content'][id - 1]
    # NLP Stuff
    blob = TextBlob(rawtext)
    #received_text2 = blob
    # blob_sentiment, blob_subjectivity = blob.sentiment.polarity, blob.sentiment.subjectivity
    #number_of_tokens = len(list(blob.words))

    stop = list()
    slist = list()
    for word in blob.words:

        if word not in stopwords.words('english'):
            stop.append(word)
            slist.append(word)
        else:
            stop.append('\u0336'.join(word) + '\u0336')

    #markstop = ' '.join(stop)

    # slist = (word for word in blob.words if word not in stopwords.words('english'))

    new_text = ' '.join(slist)

    new_blob = TextBlob(new_text)
    new_received = new_blob

    blob_sentiment, blob_subjectivity = new_blob.sentiment.polarity, new_blob.sentiment.subjectivity
    # Extracting Main Points

    #nouns = []
    # pos = []
    # neg = []
    # ntr = []



    if blob_sentiment > 0.0:
        # pos.append([format_sentence(str(new_received)), 'pos']
        tr.append((str(new_received), 'pos'))
    # else:
    #     tr.append((str(new_received), 'neg'))
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


def analyze_nb():
    #print(tr)
    print ("NB:")
    #3 kinds of sets

    for i in range(0, 10):
        t_rf.append((rf['review'][i], rf['label'][i]))


    vocabulary_t = set(chain(*[word_tokenize(i[0].lower()) for i in train]))
    feature_set_t = [({i: (i in word_tokenize(sentence.lower())) for i in vocabulary_t}, tag) for sentence, tag in
                   train]

    vocabulary_tr = set(chain(*[word_tokenize(i[0].lower()) for i in tr]))
    feature_set_tr = [({i: (i in word_tokenize(sentence.lower())) for i in vocabulary_tr}, tag) for sentence, tag in
                   tr]

    vocabulary_rfs = set(chain(*[word_tokenize(i[0].lower()) for i in t_rf]))
    feature_set_rfs = [({i: (i in word_tokenize(sentence.lower())) for i in vocabulary_rfs}, tag) for sentence, tag in
                   t_rf]


    #train_set, test_set = feature_set_tr[0:5], feature_set_tr[5:10]
    train_set, test_set = feature_set_t, feature_set_tr

    #another
    # all_words = set(word.lower() for passage in tr for word in word_tokenize(passage[0]))
    # t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in tr]

    #train_set, test_set = feature_set[0:10], feature_set[10:20]
    #SAMPLE SET
    # vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in train]))
    #
    # feature_set = [({i: (i in word_tokenize(sentence.lower())) for i in vocabulary}, tag) for sentence, tag in
    #                train]

    classifier = nbc.train(train_set)

    test_sentence = "This is the worst band!"
    featurized_test_sentence = {i: (i in word_tokenize(test_sentence.lower())) for i in vocabulary_t}
    #
    print("test_sent:", test_sentence)
    print("tag:", classifier.classify(featurized_test_sentence))
    #classifier.show_most_informative_features()
    print("Accuracy: ", nltk.classify.accuracy(classifier, test_set))

    asnb, acc = classifier.show_most_informative_features(), nltk.classify.accuracy(classifier, test_set)

    return (asnb, acc)

def analyze_snb():
    #print(tr)
    print ("SNB:")
    #enron set
    # vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in tr]))
    #
    # feature_set = [({i: (i in word_tokenize(sentence.lower())) for i in vocabulary}, tag) for sentence, tag in
    #                tr]
    #
    # print (tr)

    for i in range(0, 10):
        t_rf.append((rf['review'][i], rf['label'][i]))

    #another
    all_words = set(word.lower() for passage in train for word in word_tokenize(passage[0]))
    t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train]

    all_words_tr = set(word.lower() for passage in tr for word in word_tokenize(passage[0]))
    t_tr = [({word: (word in word_tokenize(x[0])) for word in all_words_tr}, x[1]) for x in tr]

    all_words_rf = set(word.lower() for passage in t_rf for word in word_tokenize(passage[0]))
    t_rfs = [({word: (word in word_tokenize(x[0])) for word in all_words_rf}, x[1]) for x in t_rf]



    #t_rf = [({rf['review'][0]},rf['label'][0])]

   #train_set, test_set = t_tr[0:10], t

    train_set, test_set = t, t_tr

    # print(t)
    # print(t_tr)
    # print (t_rfs)


    #train_set, test_set = feature_set[0:10], feature_set[10:20]
    #SAMPLE SET
    # vocabulary = set(chain(*[word_tokenize(i[0].lower()) for i in train]))
    #
    # feature_set = [({i: (i in word_tokenize(sentence.lower())) for i in vocabulary}, tag) for sentence, tag in
    #                train]

    classifier = nbc.train(train_set)

    test_sentence = "This is the worst band!"
    featurized_test_sentence = {word.lower(): (word in word_tokenize(test_sentence.lower())) for word in all_words}
    #
    print("test_sent:", test_sentence)
    print("tag:", classifier.classify(featurized_test_sentence))
    #classifier.show_most_informative_features()
    print("Accuracy: ", nltk.classify.accuracy(classifier, test_set))

    anb, acc = classifier.show_most_informative_features(), nltk.classify.accuracy(classifier, test_set)

    # return nltk.classify.accuracy(classifier, test_set)
    return (anb, acc)
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



