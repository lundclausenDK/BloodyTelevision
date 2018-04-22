import pandas as pd
import numpy as np

file_trump = "realDonaldTrump.csv"
file_obama = "BarackObama.csv"
data_trump = pd.read_csv(file_trump)
data_obama = pd.read_csv(file_obama)
matrix_obama = data_obama.as_matrix()
matrix_trump = data_trump.as_matrix()


def question_1():
    amount = np.size(matrix_trump[:, 0]) / 60
    print(amount)


def question_2():
    new_list = matrix_obama[0:100]
    amount = np.size(new_list[:, 0]) / 52
    print(amount)


def question_3():
    matchers_1 = ['MAKE AMERICA GREAT AGAIN', 'yes we can']
    lst_trump = matrix_trump[:, 1]
    lst_obama = matrix_obama[:, 1]
    matching_trump = [s for s in lst_trump if any(xs in s for xs in matchers_1)]
    matching_obama = [s for s in lst_obama if any(xs in s for xs in matchers_1)]
    print("Obama", matchers_1[1], len(matching_obama))
    print("Trump", matchers_1[0], len(matching_trump))


def question_4():
    matchers = ['Iran']
    trump_list = matrix_trump[:, 1]
    obama_list = matrix_obama[:, 1]
    trump_mentions = [s for s in trump_list if any(xs in s for xs in matchers)]
    obama_mentions = [s for s in obama_list if any(xs in s for xs in matchers)]
    print("trump", len(trump_mentions))
    print("obama", len(obama_mentions))


def question_5():
    matchers = ["Obamacare", "obamacare"]
    lst_trump = matrix_trump[:, 1]
    matching_trump = [s for s in lst_trump if any(xs in s for xs in matchers)]
    print("trump", len(matching_trump))
    lst_obama = matrix_obama[:, 1]
    matching_obama = [s for s in lst_obama if any(xs in s for xs in matchers)]
    print("obama", len(matching_obama))


question_1()
question_2()
question_3()
question_4()
question_5()

