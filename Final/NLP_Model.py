import pandas as pd
import string
# from collections import Counter
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

Df = pd.read_csv('S:\Projects\Web scrapping\Scraper1.csv')
# print(Df['Reviews'])
postive = []
negative = []
neutral = []
for i in Df['Reviews']:

    try:
        lst = i.split(',')
    except:
        lst = []
    if not lst:
        pos=[]
        neg=[]
        neu=[]

    if lst:
        pos=[]
        neg=[]
        neu=[]
        for words in lst:
            # print(words)
            text = words
            lower_case=text.lower()
            cleaned_text=lower_case.translate(str.maketrans('', '', string.punctuation))

            # Using word_tokenize because it's faster than split()
            tokenized_words=word_tokenize(cleaned_text, "english")
            # Removing Stop Words
            final_words=[]
            for word in tokenized_words:
                if word not in stopwords.words('english'):
                    final_words.append(word)

            # Lemmatization - From plural to single + Base form of a word (example better-> good)
            lemma_words=[]
            for word in final_words:
                word=WordNetLemmatizer().lemmatize(word)
                lemma_words.append(word)

            emotion_list=[]
            with open('emotions.txt', 'r') as file:
                for line in file:
                    clear_line=line.replace("\n", '').replace(",", '').replace("'", '').strip()
                    word, emotion=clear_line.split(':')

                    if word in lemma_words:
                        emotion_list.append(emotion)

            # print(emotion_list)
            # w=Counter(emotion_list)
            # print(w)

            def sentiment_analyse(sentiment_text):
                score=SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
                if score['neg'] > score['pos']:
                    neg.append(1)
                    # print("Negative Sentiment")
                elif score['neg'] < score['pos']:
                    pos.append(1)
                    # print("Positive Sentiment")
                else:
                    neu.append(1)
                    # print("Neutral Sentiment")
            sentiment_analyse(cleaned_text)
    print(sum(pos), sum(neg), sum(neu))
    postive.append(sum(pos))
    negative.append(sum(neg))
    neutral.append(sum(neu))


print(postive)
print(negative)
print(neutral)

Df['Postive']=postive
Df['Negative']=negative
Df['Neutral'] = neutral
Df.to_csv('S:\Projects\Web scrapping\Scraper1.csv')
print(Df[['Postive','Negative','Neutral']])

