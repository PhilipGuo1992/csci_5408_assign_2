from elasticsearch import Elasticsearch
from elasticsearch import helpers
import csv
# count how many rows
tweeter_data = open('tweets_score.csv', 'r+', encoding='utf-8')
read_tweet = csv.reader(tweeter_data)
row_count = sum(1 for row in read_tweet)
# read csv data into reader
reader = csv.DictReader(open('tweets_score.csv', 'r', encoding='utf-8'))
es = Elasticsearch() # Define a default Elasticsearch client
# code from lab.
actions = [ { "_index": "datatweets",
              "_type": "tweet",
              "_id": mm,
              "_source": {
                  "tweet": line['tweets'],
                  "sentiment" : line['sentiment'],
                  "sentiment_score" : line['score']
              }}
            for line in reader for mm in range(0, row_count - 1)]
helpers.bulk(es, actions)