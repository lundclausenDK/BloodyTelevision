# Song analysis and answers - Just run code below
import os
import urllib.request as req
import pandas as pd
import matplotlib.pyplot as plt
from urllib.parse import urlparse
from collections import Counter
from operator import itemgetter


def download(url, to=None, file_name=None):
    if to:
        if file_name is None:
            localfile = to + os.path.basename(urlparse(url).path)
        else:
            localfile = to + file_name
    elif file_name:
        localfile = file_name
    else:
        fileName = os.path.basename(urlparse(url).path)
        localfile = os.path.join('.', fileName)

    if not os.path.isfile(localfile):
        print('Downloading file to {}'.format(localfile))
        req.urlretrieve(url, localfile)


url = "https://github.com/KasperOnFire/ImpossibleTechnology/raw/master/Datasets/songdata.csv"
filename = "songdata.csv"
download(url, file_name=filename)
pd_raw_data = pd.read_csv(filename)
my_matrix = pd_raw_data.as_matrix()


# What is the most used words in the songs?
def question_1():
    song_text = my_matrix[:, 3]
    columns = ",".join(song_text)
    joined_cols = columns.split()

    # Count top 3
    top_words = Counter(joined_cols).most_common(3)

    print(top_words)

    # Lets select the 3 keys and values
    plt.bar(top_words[0][0], top_words[0][1])
    plt.bar(top_words[1][0], top_words[0][1])
    plt.bar(top_words[2][0], top_words[0][1])
    plt.title("Top 3 - Most used words in songs")
    plt.xlabel("Words")
    plt.ylabel("Occurrences")
    plt.show()


def question_2():
    my_title = my_matrix[:, 1][2]
    song_text = my_matrix[:, 3][2]
    joined_cols = song_text.split()
    my_count = Counter(joined_cols)

    print(my_title + ": ")
    print(my_count)


def question_3():
    song_text = my_matrix[:, 3]
    # Words we will search for
    dist = {'feet': 0, 'toes': 0, 'smell': 0}

    for i in range(len(song_text)):
        words = song_text[i].split()
        for j in words:
            if j in dist.keys():
                dist[j] += 1

    plt.title('3 words to search for')
    plt.bar(range(len(dist)), list(dist.values()))
    plt.xticks(range(len(dist)), list(dist.keys()))
    plt.ylabel('Occurrences')
    plt.xlabel('Our choosen words')
    plt.show()


def question_4():
    song_title = my_matrix[:, 1]
    song_text = my_matrix[:, 3]
    dist = {}

    for i in range(len(song_title)):
        dist[song_title[i]] = len(song_text[i].split())

    sorted_songs = sorted(dist.items(), key=itemgetter(1), reverse=True)
    average = sum(dist.values()) / len(dist)

    plt.title('Words per song')
    plt.bar('Most words: ' + sorted_songs[0][0], sorted_songs[0][1])
    plt.bar('Average song', average)
    plt.bar('Least words: ' + sorted_songs[-1][0], sorted_songs[-1][1])
    plt.ylabel('Numbers of words')
    plt.show()


def question_5():
    song_text = my_matrix[:, 3]
    dist = {}

    for i in range(len(song_text)):
        dist[i] = len(song_text[i].split())

    word_freq = dict(Counter(dist.values()))

    sorted_words = sorted(word_freq.items(), key=itemgetter(1), reverse=True)

    plt.title('Songs and the amount of words')
    for words, amount in sorted_words[:]:
        plt.bar(words, amount, color='grey')
    plt.ylabel('Songs')
    plt.xlabel('Words')
    plt.show()


question_1()
question_2()
question_3()
question_4()
question_5()
