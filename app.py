from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from time import ctime


from process import df
from textblob import TextBlob,Word
from nltk.corpus import stopwords

import random
import time

from nlp import process, run_nb, tr, analyze_snb, analyze_nb

import tkinter as tk
from time import sleep


app = Flask(__name__)
Bootstrap(app)


dt=ctime()



@app.route('/')
def main():
    return render_template('index.html', dt=dt)


@app.route('/dataset/view/<int:id>')
def view(id):
    #received_text2, new_received, number_of_tokens, blob_sentiment, blob_subjectivity, summary, final_time, len_of_words, pos, neg, training, test=process(id)
    received_text2, new_received, number_of_tokens, blob_sentiment, blob_subjectivity, summary, final_time, len_of_words, markstop = process(id)
    # print(pos)
    # print(neg)
    # print(training)
    return render_template('dataset_view.html', received_text=received_text2, new_received=new_received, number_of_tokens=number_of_tokens,
                           blob_sentiment=blob_sentiment, blob_subjectivity=blob_subjectivity, summary=summary,
                           final_time=final_time, len=len_of_words, dt=dt, id=id, df=df, markstop=markstop)


@app.route('/dataset/')
def dataset():
    set = []

        #set.append(tr)

    #return render_template('dataset.html', dt=dt, df=df, sentiment=sentiment)



    return render_template('dataset.html', dt=dt, df=df)


@app.route('/charts')
def charts():
    return render_template('charts.html',dt=dt)

@app.route('/naivebayes')
def nb():
    # if tr == []:
    #     for i in range(0, 10):
    #         i=i+1
    #         run_nb(i)
    #
    #
    # anb, accnb, t, dfcol = analyze_nb()
    # asnb, accsnb, t2, dfcol2 = analyze_snb()
    #
    # ft = t+t2

    anb, accnb, t, dfcol = "", "", "", ""
    asnb, accsnb, t2, dfcol2 = "","","",""
    ft=0

    #print("NB: ")
    #anb = analyze_nb()
    #analyze_nb()
    #print("S-NB: ")
    #analyze_snb()
    return render_template('nb.html',dt=dt, anb=anb, asnb = asnb, accnb = accnb, accsnb = accsnb, ft=ft, df=df, dfcol=dfcol, dfcol2=dfcol2)

@app.route('/naivebayes/train')
def bp_nb():
    if tr == []:
        for i in range(0, 10):
            run_nb(i)

    anb, accnb, t, dfcol = analyze_nb()
    asnb, accsnb, t2, dfcol2 = analyze_snb()


    return render_template('nb.html',dt=dt, anb=anb, asnb = asnb, accnb = accnb, accsnb = accsnb, t=t, t2=t2, df=df, dfcol=dfcol, dfcol2=dfcol2)

if __name__ == '__main__':
    app.run(debug=True)
