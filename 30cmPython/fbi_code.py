import xlrd
import matplotlib.pyplot as plt
import requests
import numpy as np
from operator import itemgetter

urls = [{"url" :"https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/1tabledatadecoverviewpdf/table_1_crime_in_the_united_states_by_volume_and_rate_per_100000_inhabitants_1994-2013.xls",
"name": "table.xls"},
{"url": "https://ucr.fbi.gov/crime-in-the-u.s/2013/crime-in-the-u.s.-2013/tables/table-8/table_8_offenses_known_to_law_enforcement_by_state_by_city_2013.xls",
 "name": "geo2013.xls"},
{"url": "https://ucr.fbi.gov/crime-in-the-u.s/2010/crime-in-the-u.s.-2010/tables/table-8/table_8_offenses_known_to_law_enforcement_by_state_by_city_2010.xls",
"name": "geo2010.xls"}]

#file download
def download_file(url, filename=None):
    local_filename = ""
    if(filename == None):
        local_filename = url.split('/')[-1]
    else:
        local_filename = filename
        
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: 
                f.write(chunk)
    return local_filename
#downloading all files from urls, THIS DOESNT WORK, AND ISNT USED AT PRESENT TIME.
"""
for url in urls:
    download_file(url['url'], url['name'])
"""
#Svar til spørgsmål 1
def question_1():
    
    filename = "table.xls"
    
    wb = xlrd.open_workbook(filename)
    
    sheet = wb.sheets()[0]
    
    '''
    for n in range(sheet.nrows):
        rowvals = sheet.row_values(n)
        print(rowvals)
    '''
    start = 4
    slut = 24
    
    r = sheet.col_values(0)[start:slut]
    violent = sheet.col_values(2)[start:slut]
    property_crime = sheet.col_values(12)[start:slut]

    data = []
    for i in range(sheet.nrows):
        data.append(sheet.row_values(i))
    
    better_datax = []
    better_datay = []
    for el in r:
        if len(str(el)) > 4:
            el = str(el)[0:4]
            better_datax.append(el)
        else:
            better_datax.append((el))
    
    for i in range(len(violent)):
        sum = violent[i] + property_crime[i]
        better_datay.append(sum)
    
    
    #print(better_datax)
    #print(better_datay[4:24])
    
    plt.bar(better_datax, better_datay)
    plt.title('Question 1: Has the crime decreased or increased over the last 20 years?')
    plt.xlabel('year')
    plt.ylabel('Calculated Crime')
    plt.show()
    

#svar 2
def question_2():

    filename = "table.xls"
 
    wb = xlrd.open_workbook(filename)
    
    sheet = wb.sheets()[0]
   
    robberies = []
    murder_n_stuff = []
    rapes = []
    crimes = []
    assaults = []
    prop_crime = []
    for el in sheet.col_values(12)[4:24]:
        prop_crime.append(el)
    for el in sheet.col_values(10)[4:24]:
        assaults.append(el)
    for el in sheet.col_values(8)[4:24]:
        robberies.append(el)
    for el in sheet.col_values(6)[4:24]:
        rapes.append(el)
    for el in sheet.col_values(4)[4:24]:
        murder_n_stuff.append(el)
    for el in sheet.col_values(2)[4:24]:
        crimes.append(el)
    
    plt.title('Question 2: Has the type of crime changed?')
    plt.xlabel('year')
    plt.ylabel('Crime')
    time = list(range(1994, 2013+1))

    plt.plot(time, crimes, label='Crimes')
    plt.plot(time, murder_n_stuff, label='Murders')
    plt.plot(time, rapes, label='Rapes')
    plt.plot(time, robberies, label='Robberies')
    plt.plot(time, assaults, label='Assaults')
    plt.plot(time, prop_crime, label='Property Crime')
    plt.legend()
    plt.show()

#svar 3
def question_3():
    # Lets get data
    start_year = "geo2010.xls"
    end_year = "geo2013.xls"

    wb_start = xlrd.open_workbook(start_year)
    wb_end = xlrd.open_workbook(end_year)

    sheet1 = wb_start.sheets()[0]
    sheet2 = wb_end.sheets()[0]

    violent_crime_by_state_2010 = {}
    violent_crime_by_state_2013 = {}

    first_state_row1 = 4
    first_state_row2 = 4

    temp_sum_up1 = 0
    temp_sum_up2 = 0

    stored_state1 = ""
    stored_state2 = ""

    for i in range(4, len(sheet1.col_values(3)[4:])):
        active_state = sheet1.col_values(0)[first_state_row1]

        if active_state != "" and active_state != stored_state1 and temp_sum_up1 != 0:
            violent_crime_by_state_2010[active_state] = temp_sum_up1
            temp_sum_up1 = 0

        if sheet1.col_values(3)[i] != "":
            temp_sum_up1 += sheet1.col_values(3)[i]

        stored_state1 = active_state
        first_state_row1 += 1

    for i in range(4, len(sheet2.col_values(3)[4:])):
        active_state = sheet2.col_values(0)[first_state_row2]

        if active_state != "" and active_state != stored_state2 and temp_sum_up2 != 0:
            violent_crime_by_state_2013[active_state] = temp_sum_up2
            temp_sum_up2 = 0

        if sheet2.col_values(3)[i] != "":
            temp_sum_up2 += sheet2.col_values(3)[i]

        stored_state2 = active_state
        first_state_row2 += 1

    x1 = sorted(violent_crime_by_state_2010.items(), key=itemgetter(1), reverse=True)
    x2 = sorted(violent_crime_by_state_2013.items(), key=itemgetter(1), reverse=True)

    # Lets print data in chart
    state1 = x1[0][0]
    state2 = x1[1][0]
    state3 = x1[2][0]

    stats2010_1 = x1[0][1]
    stats2010_2 = x1[1][1]
    stats2010_3 = x1[2][1]

    stats2013_1 = x2[0][1]
    stats2013_2 = x2[1][1]
    stats2013_3 = x2[2][1]

    n_groups = 3

    year2010 = (stats2010_1, stats2010_2, stats2010_3)
    year2013 = (stats2013_1, stats2013_2, stats2013_3)

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.30

    opacity = 0.4

    ax.bar(index, year2010, bar_width,
                    alpha=opacity,
                    color='b')

    ax.bar(index + bar_width, year2013, bar_width,
                    alpha=opacity,
                    color='r')

    plt.title('Question 3: Has the crime moved to from one area to another?')
    ax.set_xlabel('Top 3 by states')
    ax.set_ylabel('Crime incidents in total')
    ax.set_title('Crime by area')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels((state1, state2, state3))
    plt.legend(["2010", "2013"])

    fig.tight_layout()
    plt.show()


   
    
#svar 4
def question_4():

    def get_color(crime):
        return {
            'theft': 'red', 
            'auto_theft': 'purple', 
            'arson': 'yellow'
        }[crime]

    filename = "geo2013.xls"

    wb = xlrd.open_workbook(filename)
    sheets = wb.sheets()[0]

    stored_state = sheets.cell_value(4, 0)

    states_crime = {}
    theft, auto_theft, arson = 0, 0, 0

    for row in range(4, sheets.nrows):
        if sheets.cell_value(row, 0) != '' and not sheets.cell_value(row, 0)[0].isdigit():
            active_state = sheets.cell_value(row,0)
            
        if active_state != stored_state:
            states_crime[stored_state] = {'theft': theft, 'auto_theft': auto_theft, 'arson': arson}
            theft, auto_theft, arson = 0, 0, 0

        if stored_state == active_state or sheets.cell_value(row, 0) == '':
            if isinstance(sheets.cell_value(row, 11), float):
                theft += sheets.cell_value(row, 11)
            if isinstance(sheets.cell_value(row, 12), float):
                auto_theft += sheets.cell_value(row, 12)
            if isinstance(sheets.cell_value(row, 13), float):
                arson += sheets.cell_value(row, 13)
            
        stored_state = active_state


    i = 0    
    for _, crime in states_crime.items():
        width = 0
        for crime, value in crime.items():
            plt.bar(i + width, value, label=crime, color=get_color(crime))
            width += 0.025
        i += 1
    
    plt.title('Question 4: Is there a connection between type of crimes and locations?')
    plt.xticks(range(len(states_crime.keys())), states_crime.keys(), rotation='vertical')
    plt.legend(['Larceny', 'Vehicle theft', 'Arson'])
    plt.show()   
    
#svar 5
def question_5():

    filename = "./table.xls"

    wb = xlrd.open_workbook(filename)
    sheet = wb.sheet_by_index(0)

    murder = sheet.col_values(4)[4]
    rape = sheet.col_values(6)[4]
    robbery = sheet.col_values(8)[4]
    assault = sheet.col_values(10)[4]
    burgulary = sheet.col_values(14)[4]
    larceny = sheet.col_values(16)[4]
    vehicle_theft = sheet.col_values(18)[4]

    plt.bar(1, murder)
    plt.bar(2, rape)
    plt.bar(3, robbery)
    plt.bar(4, assault)
    plt.bar(5, burgulary)
    plt.bar(6, larceny)
    plt.bar(7, vehicle_theft)

    plt.xticks(list(range(1,7+1)), ['Murder', 'Rape', 'Robbery', 'Assault', 'Burgulary', 'Larceny', 'Vehicle theft'])

    plt.title('Question 5: Which year was the most crime and what crime occured most times? (1994)')
    plt.xlabel('Type of Crime')
    plt.ylabel('Count of Type')
    plt.show()


def main():
    question_1()
    question_2()
    question_3()
    question_4()
    question_5()

if __name__ == '__main__':
    main()