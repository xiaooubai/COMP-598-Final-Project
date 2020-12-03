"""
Script for computing tf-idf for each topic and writing results to separate tsv files
"""

import pandas as pd
import os.path as osp
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk import pos_tag
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

df = pd.read_csv(osp.join('..' , 'data' , 'Final_data' , 'final_data.csv'))


def main():
    preprocess()
    #print(df['coding'])
    topics = ['policy' , 'economy_climate', 'lawsuit' , 'covid', 'transition' , 'dissatisfaction' , 'vote' , 'discrimination']
    vector = TfidfVectorizer()

    for topic in topics:
        tmp_df = df[df['coding'] == topic]

        train_x = vector.fit_transform(tmp_df['title'].map(' '.join))

        result = pd.DataFrame(train_x[0].T.todense() , index=vector.get_feature_names(), columns=['TF-IDF'])
        result = result.sort_values('TF-IDF' , ascending=False)
        print('tfidf results for ' , topic)
        result = result.head(10)
        filename = f'{topic}.tsv'
        result.to_csv(osp.join('..' , 'data', 'Results' , filename), sep='\t')

def preprocess():
    #tokenizes, lemmatizes, and changing every character to lower case the data and removes the stop words
    #we can have a better understanding of the data by this approach(e.g., "Vote" and "vote" would considered different words withput pre-processing)

    df['title'] = [entry.lower() for entry in df['title']]

    df['title'] = [word_tokenize(entry) for entry in df['title']]

    #removes the stopwords
    stop = stopwords.words('english')
    df['title'] = df['title'].apply(lambda x: [item for item in x if item not in stop])

    tagmap = defaultdict(lambda: wn.NOUN)
    tagmap['J']= wn.ADJ
    tagmap['V']= wn.VERB
    tagmap['R'] = wn.ADV

    for index, entry in enumerate(df['title']):
        Final_words = []
        lemmatized_word = WordNetLemmatizer()
        for word, tag in pos_tag(entry):
            if word.isalpha():
                word_final = lemmatized_word.lemmatize(word, tagmap[0])
                Final_words.append(word_final)
        df.loc[index, 'Text_final'] = str(Final_words)







if __name__ == '__main__':
    main()