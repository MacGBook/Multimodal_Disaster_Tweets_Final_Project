from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import csv

file_path = "text.csv"

# LOAD MODEL ONCE
roberta = "cardiffnlp/twitter-roberta-base-sentiment"
model = AutoModelForSequenceClassification.from_pretrained(roberta)
tokenizer = AutoTokenizer.from_pretrained(roberta)

labels = ['Negative', 'Neutral', 'Positive']

with open(file_path, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    data = [row for row in csv_reader]

string_list = [row[0] for row in data]

second_string_list = ["TommyGShow: Burlington County offers to purchase landslide-damaged properties in Florence http://t.co/xgguElyxyi"]

for tweet in second_string_list:

    # preprocess tweet
    tweet_words = []

    for word in tweet.split(" "):
        if word.startswith("@") and len(word) > 1:
            word = "@user"
        elif word.startswith("http"):
            word = "http"

        tweet_words.append(word)

    tweet_proc = " ".join(tweet_words)

    encoded_tweet = tokenizer(tweet_proc, return_tensors="pt")

    print("##########################")
    print(encoded_tweet)

    # sentiment analysis
    output = model(**encoded_tweet)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    for label, score in zip(labels, scores):
        print(label, score)

    row = []
    for label, score in zip(labels, scores):
        row.extend([label, float(score)])

    with open("test_results.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(row)