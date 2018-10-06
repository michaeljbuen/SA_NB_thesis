from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from time import ctime


from process import df
from textblob import TextBlob,Word
from nltk.corpus import stopwords

import random
import time

from nlp import process, format_sentence




app = Flask(__name__)
Bootstrap(app)


dt=ctime()



@app.route('/')
def main():
    return render_template('index.html', dt=dt)


@app.route('/dataset/view/<int:id>')
def view(id):
    #received_text2, new_received, number_of_tokens, blob_sentiment, blob_subjectivity, summary, final_time, len_of_words, pos, neg, training, test=process(id)
    received_text2, new_received, number_of_tokens, blob_sentiment, blob_subjectivity, summary, final_time, len_of_words = process(id)
    # print(pos)
    # print(neg)
    # print(training)
    return render_template('dataset_view.html', received_text=received_text2, new_received=new_received, number_of_tokens=number_of_tokens,
                           blob_sentiment=blob_sentiment, blob_subjectivity=blob_subjectivity, summary=summary,
                           final_time=final_time, len=len_of_words, dt=dt, id=id, df=df)


@app.route('/dataset/')
def dataset():
    #sentiment = []
    #for i in range(0, len(df)):
        #i=i+1
       # sentiment.append(process(i)[3])

    #return render_template('dataset.html', dt=dt, df=df, sentiment=sentiment)
    return render_template('dataset.html', dt=dt, df=df)


@app.route('/charts')
def charts():
    return render_template('charts.html',dt=dt)


if __name__ == '__main__':
    app.run(debug=True)
