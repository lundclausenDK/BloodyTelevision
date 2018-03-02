#import getter
import pandas as pd
import matplotlib.pyplot as plt
import collections
import numpy as np
from operator import itemgetter

#getter.download("https://raw.githubusercontent.com/PatrickFenger/pythonAssignments/master/KoreanConflict.csv")
filename = 'KoreanConflict.csv'
pd_raw_data = pd.read_csv(filename)
my_matrix = pd_raw_data.as_matrix()


def question_1():
    marine_corps = (my_matrix[:,3] == "MARINE CORPS")
    air_force = (my_matrix[:,3] == "AIR FORCE")
    army = (my_matrix[:,3] == "ARMY")
    plt.bar(["Marine Coprs","Air Force","Army"], [len(my_matrix[marine_corps]),len(my_matrix[air_force]),len(my_matrix[army])])
    plt.show()

    
def question_2():
    active_guard = (my_matrix[:, 2] == "ACTIVE - GUARD/RESERVE")
    active_regular = (my_matrix[:, 2] == "ACTIVE - REGULAR")
    selected_service = (my_matrix[:, 2] == "SELECTED SERVICE")
    plt.bar(["active-guard", "active-regular", "selected-service"], [len(my_matrix[active_guard]), len(my_matrix[active_regular]), len(my_matrix[selected_service])])
    plt.show()


def question_3():
    # this was just for fun to see how to gather names in the data to use directly so i could write less, also i could see directly what names to expect
    name_list = []
    name_list = my_matrix[:,15]
    name_list = [item for item, count in collections.Counter(name_list).items() if count > 0 and isinstance(item,str)]
    #print(name_list)
    
    #here it starts
    white_people = my_matrix[:,15] == name_list[0]
    black_people = my_matrix[:,15] == name_list[1]
    us_natives = my_matrix[:,15] == name_list[2]
    islanders = my_matrix[:,15] == name_list[3]
    asians = my_matrix[:,15] == name_list[4]

    list_amount = [len(my_matrix[white_people]),len(my_matrix[black_people]),len(my_matrix[us_natives]),len(my_matrix[islanders]),len(my_matrix[asians])]
    plt.bar(["white","black","natives","islanders","asians"],list_amount)
    plt.show()


def question_4():
    divisions = []
    divisions = my_matrix[:,18]
    divisions_names = [item for item, count in collections.Counter(divisions).items() if count > 0 and isinstance(item,str)]
    #print("amount of divisions:",len(divisions_names))

    division_cas_mask = (my_matrix[:,23] == "DECLARED DEAD")
    #print(len(my_matrix[division_cas_mask]))
    division_dic = {}
    for division in pd_raw_data['DIVISION'].values:
        try: 
            if division is not np.nan:
                division_dic[division] += 1
        except:
            division_dic[division] = 1
    temp_dic = sorted(division_dic.items(), key = itemgetter(1), reverse = True)
    ordered_dic = {}
    for item in temp_dic[:3]:
        ordered_dic[item[0]] = item[1]

    plt.bar(ordered_dic.keys(), ordered_dic.values())
    plt.show()


def question_5():
    state_dict = {}
    for state in pd_raw_data['HOME_STATE'].values:
        try:
            state_dict[state] += 1
        except:
            state_dict[state] = 1

    sorted_dict = sorted(state_dict.items(), key=itemgetter(1), reverse=True)
    #print(sorted_dict)
    ordered_dict = {}
    for item in sorted_dict[0:3]:
        ordered_dict[item[0]] = item[1]

    plt.bar(ordered_dict.keys(),ordered_dict.values())
    plt.xticks(rotation="horizontal")
    plt.show()



question_1()
question_2()
question_3()
question_4()
question_5()

