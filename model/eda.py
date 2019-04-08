import pandas as pd
import pdb
import pickle
import re
pd.options.display.max_columns = 30
map_student = pd.read_pickle("data/fall2017-fixed/map_student.pkl")

data = pd.read_pickle("data/fall2017-fixed/AllData.pkl")
data['Problem Name'].unique()
stepnames = data['Step Name'].unique()
data['Anon Student Id'].unique()
def print_student_code(data, problem_name, student_num):
    c = 0
    valid_c = 0
    last_codesnap = ""
    for i in range(len(data.index)):
        if data.ix[i, 'Anon Student Id'] == student_num:
            if data.ix[i, 'Problem Name'] == problem_name:
                c = c + 1
                if type(data.ix[i, -1]) != float:
                    filename = "generated-data/student" + str(student_num) + "-" + problem_name +'.txt'
                    print("------------------------------------------------",  file = open(filename, 'a'))
                    print('NUMBER ', c, file = open(filename, 'a'))
                    print("Row: ", data.ix[i, "Row"],  file = open(filename, 'a'))
                    stepname = data.ix[i, 'Step Name']
                    print("Step Name: ", stepname,  file = open(filename, 'a'))
                    if re.search('grabbed', stepname):
                        continue
                    else:
                        this_codesnap = data.ix[i, -1]
                        for j in range(len(this_codesnap)):
                            if j >= len(last_codesnap) or this_codesnap[j] != last_codesnap[j]:
                                this_codesnap = this_codesnap[:j] +"!!!!!" + this_codesnap[j:]
                                break
                    valid_c = valid_c + 1
                    last_codesnap = data.ix[i, -1]
                    print(this_codesnap,  file = open(filename, 'a'))

    print("all valid code count: ",valid_c,  file = open(filename, 'a'))
print_student_code(data,'polygonMakerLab', 15)