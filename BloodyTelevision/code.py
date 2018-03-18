# IMDB
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from operator import itemgetter
import numpy as np

# filename is a variable which is also used in the webget
#pd_raw_data = pd.read_csv(filename, sep='\t')
pd_raw_data = pd.read_csv("data.tsv", delimiter="\t", encoding="utf-8", dtype={"genres": str, "startYear": str}, sep='\t')
my_matrix = pd_raw_data.as_matrix()


def question_1():
    start_year = my_matrix[:,5]
    title_type = my_matrix[:,1]
    dist = {}

    for i in range(len(start_year)):
        if start_year[i] in dist and title_type[i] == 'movie':
            dist[start_year[i]] += 1
        elif not start_year[i] in dist and title_type[i] == 'movie':
            dist[start_year[i]] = 1
    
    sorted_years = sorted(dist.items(), key=itemgetter(1), reverse=True)

    plt.title('Top 20 years with most movie releases')
    for year, count in sorted_years[1:21]:
        plt.bar(year, count)

    plt.ylabel('Amount')
    plt.xlabel('Year')
    plt.show()


def question_2():
    end_year = my_matrix[:,6]
    count = np.unique(end_year, return_counts=True)
    ziped = list(zip(count[0], count[1]))
    sorted_list = sorted(ziped, key=itemgetter(1), reverse=True)
    print('The year that most series ended was {} with a count of {}'.format(sorted_list[1][0], sorted_list[1][1]))


def question_3():
    types = my_matrix[:, 1]
    runtimes = my_matrix[:, 7]
    genres = my_matrix[:, 8]

    indexes = [i for i,x in enumerate(types) if x == 'movie']
    
    genres_runtime_dict = {}
    genres_movie_count_dict = {}
    slash_n = str(chr(92))+"N"
    for index in indexes:
        if genres[index] in genres_runtime_dict and str(runtimes[index]) != slash_n:
            genres_runtime_dict[genres[index]] += int(runtimes[index])
            genres_movie_count_dict[genres[index]] += 1
        elif str(runtimes[index]) != slash_n:
            genres_runtime_dict[genres[index]] = int(runtimes[index])
            genres_movie_count_dict[genres[index]] = 1    

    #calculate average runtime
    calculated_dict = {}
    for key, value in genres_runtime_dict.items():
        calculated_dict[key] = int(value)/genres_movie_count_dict[key]

    calculated_dict_sorted = sorted(calculated_dict.items(), key=itemgetter(1), reverse=True)

    i = 0
    x = list(range(10))
    for _, value in calculated_dict_sorted[:10]:
        plt.bar(x[i], value)
        i += 1
    plt.xticks(x, [key for key, _ in calculated_dict_sorted[:10]], rotation=70)
    plt.subplots_adjust(bottom=0.35)
    plt.title('Top 10 of avarage genre runtime in movies')
    plt.ylabel('average runtime')
    plt.xlabel('genre')
    plt.legend([value for _, value in calculated_dict_sorted[:10]])
    plt.show()


def question_4():
    # Lets select the relevant column
    my_type = my_matrix[:, 1]
    genres = my_matrix[:, 8]

    # Lets create a new dictionary
    my_list = dict(zip(my_type, genres))

    # We only want the top of the list, and counted on the fly
    data = dict(Counter(my_list))

    print("Which genre covers the most movies?: " + data["movie"])
    

def question_5():
    is_adult = my_matrix[:, 4]
    runtime = my_matrix[:, 7]
    title_type = my_matrix[:, 1]
    total_time_adult = 0
    amount_adult = 0
    total_time = 0
    amount = 0

    for i in range(len(is_adult)):
        if is_adult[i] == 1 and not runtime[i] == '\\N' and title_type[i] == 'movie':
            total_time_adult += int(runtime[i])
            amount_adult += 1
        elif is_adult[i] == 0 and not runtime[i] == '\\N' and title_type[i] == 'movie':
            total_time += int(runtime[i])
            amount += 1

    average_adult = total_time_adult / amount_adult
    average = total_time / amount
    plt.title('Average length of an adult movies vs non-adult movies')
    plt.bar('Average adult movie', average_adult, align='center')
    plt.bar('Average non-adult movie', average, align='center')
    plt.ylabel('Runtime Minutes')
    plt.show()


question_1()
question_2()
question_3()
question_4()
question_5()
