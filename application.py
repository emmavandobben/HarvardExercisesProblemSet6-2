#!/usr/bin/env python3

from flask import Flask, redirect, render_template, request, url_for
from analyzer import Analyzer
import helpers
import os
import sys

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    
    #A LOT OF CODE DUPLICATION!
    # absolute paths to positive and negative lists.
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    
    # instantiate analyzer
    analyzer = Analyzer(positives, negatives)

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, count=99)
    if tweets is None:
        return redirect(url_for("index"))
        
    positive = 0
    negative = 0
    neutral = 0
    for tweet in tweets:
        score = analyzer.analyze(tweet)
        totalScore = score
        if score > 0:
            positive += 1
        elif score < 0:
            negative += 1
        else:
            neutral += 1
        totalScore += 1
    
    positive, negative, neutral = int((positive/totalScore)*100), int((negative/totalScore)*100), int((neutral/totalScore)*100)

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)




#screen_name from get request
#to index if missing
#get tweets

#initialize analyzer 

#interact with the web. render templates and pass in actual values. 
