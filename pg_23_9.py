import csv

print()
# method 1 -----------------------------
with open('E:\Alex\class_test.csv') as data_file:
    data = csv.reader(data_file)
    data_lst = list(data)
    print(data_lst)

    print()
    for row in data_lst:
        print(row)

    print()
    # case 1 ----------------------------------
    dct_hd = {}
    for i in range(len(data_lst[0])):
        dct_hd[data_lst[0][i]] = [row[i] for ind, row in enumerate(data_lst) if ind > 0]
    print(dct_hd)

    print()
    # case 2 ----------------------------------
    dct_hd = {data_lst[0][i] : [row[i] for ind, row in enumerate(data_lst) if ind > 0] for i in range(len(data_lst[0]))}
    print(dct_hd)

print()
# method 2 -----------------------------
import pandas

pd_data = pandas.read_csv('E:\Alex\Python\weather.csv')
print(pd_data)

print()
print(pd_data['SN'])

print()
print(pd_data['Days'])

print()
print(pd_data['Temperature'])

print()
print(pd_data['Condition'])

print()
pd_data_dict = pd_data.to_dict()
print(pd_data_dict)

# ------------------------------------------
data_dct_1 = {
    'students' : ['John', 'Derrick', 'Nathan'],
    'ages' : [24, 28, 25]
}

data_dct_2 = {
    'trainees' : ['Adil', 'Joydeep', 'Salman'],
    'ages' : [37, 24, 27]
}

data_1 = pandas.DataFrame(data_dct_1)
data_1.to_csv('class.csv')

data_2 = pandas.DataFrame(data_dct_2)
data_2.to_csv('batch35.csv')
