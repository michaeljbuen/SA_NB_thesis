from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from time import ctime


from process import df
from textblob import TextBlob,Word
from nltk.corpus import stopwords

import random
import time




app = Flask(__name__)
Bootstrap(app)


dt=ctime()


@app.route('/')
def main():
    return render_template('index.html', dt=dt)





@app.route('/dataset/view/<int:id>')
def view(id):
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

    for word, tag in blob.tags:
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


    return render_template('dataset_view.html', received_text=received_text2, new_received=new_received, number_of_tokens=number_of_tokens,
                           blob_sentiment=blob_sentiment, blob_subjectivity=blob_subjectivity, summary=summary,
                           final_time=final_time, len=len_of_words, dt=dt, id=id, df=df)


@app.route('/dataset/')
def dataset():
    return render_template('dataset.html', dt=dt, df=df)


@app.route('/charts')
def charts():
    return render_template('charts.html',dt=dt)


if __name__ == '__main__':
    app.run(debug=True)
