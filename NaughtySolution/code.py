# FIFA QUESTIONS

import sys
#change this to the correct path of you lib folder
sys.path.append('../../')
from lib import webget
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

url = "https://www.dropbox.com/s/42fpykx4kdoptvu/complete.csv?dl=1"
filename = "fifa_playes.csv"
webget.download(url, file_name=filename)
pd_raw_data = pd.read_csv(filename)
my_matrix = pd_raw_data.as_matrix()

def question_1():
    clubs = my_matrix[:, 3]
    values = my_matrix[:,  16]
    dist = {}

    for i in range(len(clubs)):
        if clubs[i] in dist:
            dist[clubs[i]] += values[i]
        else: 
            dist[clubs[i]] = values[i] 

    sorted_clubs = sorted(dist.items(), key=itemgetter(1), reverse=True)
    
    plt.subplot(2,1,1)
    plt.title('Top 3 teams by value')
    for club, value in sorted_clubs[:3]:
        plt.bar(club, value)
    
    plt.subplot(2,1,2)
    plt.title('Bottom 3 teams by value')
    for club, value in sorted_clubs[-4:]:
        plt.bar(club, value)

    plt.show()


def question_2():
    branches, count = np.unique(my_matrix[:, 14], return_counts=True)
    sorted_nationalities = sorted(dict(zip(branches, count)).items(), key=itemgetter(1), reverse=True )
    top_nations = {}
    for item in sorted_nationalities[:10]:
        top_nations[item[0]] = item[1]
    plt.pie(top_nations.values(), labels=top_nations.keys(), autopct='%1.0f%%', explode=(0.1, 0.04, 0.03, 0, 0, 0, 0, 0, 0, 0))
    plt.legend(top_nations.values(), title="Number of players", loc=4, bbox_to_anchor=(1,0),bbox_transform=plt.gcf().transFigure)
    plt.title("Percent of Top 10 of nations")
    plt.subplots_adjust(left=0.05, bottom=0.1, right=0.65)
    plt.show()


def question_3():
    players = my_matrix[:, 1]
    values = my_matrix[:, 16]
    releases = my_matrix[:, 18]
    dist = {}
    for i in range(len(players)):
        dist[players[i]] = releases[i] - values[i]

    sorted_players = sorted(dist.items(), key=itemgetter(1), reverse=True)
    # Start x = values

    for player, val in sorted_players[:10]:
        plt.bar(player, val)
    
    plt.show()


def question_4():
    age_freq = dict(Counter(my_matrix[:, 6]))
    height_freq = dict(Counter(my_matrix[:, 9]))
    weight_freq = dict(Counter(my_matrix[:, 10]))
    
    # Lets make art
    # print(age_freq)
    # print(height_freq)
    # print(weight_freq)
    
    age = list(age_freq.keys())
    height = list(height_freq.keys())
    weight = list(weight_freq.keys())
    
    age_values = list(age_freq.values())
    height_values = list(height_freq.values())
    weight_values = list(weight_freq.values())
    
    plt.bar(range(len(age_freq)), age_values, tick_label=age)
    plt.bar(range(len(height_freq)), height_values, tick_label=height)
    plt.bar(range(len(weight_freq)), weight_values, tick_label=weight)
    plt.title("Frequency diagram - FIFA players")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.xticks(rotation=90)
    plt.legend(["Age", "Height", "Weight"])
    plt.show()


def question_5():
    values = sum(my_matrix[:,  16]) / len(my_matrix[:, 16])
    wages = sum(my_matrix[:,  17]) / len(my_matrix[:, 17])
    plt.bar('Value in EUR',values)
    plt.bar('Wages in EUR',wages)
    plt.show()

if __name__ == '__main__':
    question_1()
    question_2()
    question_3() 
    question_4()
    question_5()



#new webget
import os
import urllib.request as req
from urllib.parse import urlparse

def download(url, to=None, file_name=None):
    """Download a remote file specified by a URL to a 
    local directory.
     :param url: str
        URL pointing to a remote file.
     :param to: str
        Local path, absolute or relative, with a filename 
        to the file storing the contents of the remote file.
    """

    # TODO: Implement me!
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

    print('Downloading file to {}'.format(localfile))

    if not os.path.isfile(localfile):
        req.urlretrieve(url, localfile)



