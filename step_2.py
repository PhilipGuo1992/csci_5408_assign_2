import csv
import nltk
from nltk.corpus import sentiwordnet as swn


with open('tweets.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    posScore = 0
    negScore = 0
    count = 0
    with open('tweets_score.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(['tweets', 'sentiment', 'score'])

        for row in csv_reader:
            sentence = row[-1]
            tokens = nltk.word_tokenize(sentence)
            for token in tokens:
                synsets = swn.senti_synsets(token)
                count = count+1
                for synst in synsets:
                    posScore = posScore + synst.pos_score()
                    negScore = negScore + synst.neg_score()
            if posScore > negScore:
                sentiment = 'positive'
                score = posScore/count
            elif negScore > posScore:
                sentiment = 'negative'
                score = -negScore/count
            elif negScore == posScore:
                sentiment = 'neutral'
                score = 0
            posScore = 0
            negScore = 0
            count = 0
            csv_writer.writerow([row, sentiment, score])




