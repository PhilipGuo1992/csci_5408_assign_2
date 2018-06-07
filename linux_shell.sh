# chmod u+x filename.sh
# ./finename.sh

# 1 extracte data from Twitter
python assignment2_task1.py

# perform sentiment analysis on the data
python task2.py

# load output into ElasticSearch
python BulkInsert.py
