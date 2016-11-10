"""
This file analyzes sentiment data mined on November 8th, 2016, regarding
the 2016 Presidential Election. The files store either a pos or a neg, describing
the sentiment of a tweet that mentions President elect Donald Trump. Some of the data
mining code was take from https://pythonprogramming.net/sentiment-analysis-module-nltk-tutorial/
"""
#Files opened for reading
sent_745pm = open("trump_sentiment1945.txt", "r")
sent_847pm = open("trump_sentiment2047.txt", "r")
sent_930pm = open("trump_sentiment2130.txt", "r")
sent_1008pm = open("trump_sentiment2208.txt", "r")
sent_1045pm = open("trump_sentiment2245.txt", "r")
sent_1215am = open("trump_sentiment0015.txt", "r")

#Global analysis variables declared
total_positive = 0
total_negative = 0
total_tweets = 0

#Function that counts +/- sentiment, and displays sentiment and percentages to the console
def analyze_sentiment(infile, start_time, finish_time):
    #Variables initialized
    positive = 0
    negative = 0
    total = 0

    #Reads every line of the file; increments positive/negative
    while True:
        line = infile.readline()
        if not line: break
        if line == "pos\n":
            positive += 1
            total += 1
        elif line == "neg\n":
            negative += 1
            total += 1

    #Global variables updated
    global total_tweets
    global total_positive
    global total_negative
    total_tweets += total
    total_positive += positive
    total_negative += negative

    #Percentages calculated
    percent_plus = float(positive) / float(total) * 100
    percent_neg = float(negative) / float(total) * 100

    #Analyzes data
    print("Inbetween {} and {}: ").format(start_time, finish_time)
    print("There were {} total tweets").format(total)
    print("There were {} positive tweets, and {} negative tweets").format(positive, negative)
    print("That means that {} percent were positive, and {} were negative").format(percent_plus, percent_neg)
    print("Remember that the classifier is only 70 percent accurate")
    print("\n")
    infile.seek(0)

##############

#Sentiment analyzed from gathered data, hour by hour (ish. I was busy)
analyze_sentiment(sent_745pm, 730, 745)
analyze_sentiment(sent_847pm, 830, 847)
analyze_sentiment(sent_930pm, 847, 930)
analyze_sentiment(sent_1008pm, 930, 1008)
analyze_sentiment(sent_1045pm, 1008, 1045)
print("Sentiment after Trump declared winner: \n")
analyze_sentiment(sent_1215am, 1215, 100)

#Totals calculated and displayed
total_percent_plus = float(total_positive) / float(total_tweets) * 100
total_percent_neg = float(total_negative) / float(total_tweets) * 100
print("In total, there were {} tweets about Trump- {} positive, {} negative").format(total_tweets, total_positive, total_negative)
print("That gives us {} percent positive, and {} percent negative").format(total_percent_plus, total_percent_neg)

#Files closed after being read
sent_745pm.close()
sent_847pm.close()
sent_930pm.close()
sent_1008pm.close()
sent_1045pm.close()
sent_1215am .close()
