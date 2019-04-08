import pandas as pd
import pdb
import pickle

pd.options.display.max_columns = 30
data = pd.read_csv('data/fall2017-fixed/AllData.txt', sep="\t", header=0, index_col= 0)

data = data.sort_values(['Anon Student Id', 'Time'], ascending = [1, 1]).reset_index(drop = False)
lastStudent = ""
new_id = 0
map_student = []
for i in range(len(data.index)):
    # i = 1
    student = data.ix[i, 'Anon Student Id']
    if (student != lastStudent):
        student = data.ix[i, 'Anon Student Id']
        map_student.append({"Anon Student Id": student, "New ID": new_id})
        new_id = new_id + 1
    lastStudent = student
    if str(data.ix[i, -1]) != "nan":
        data.ix[i, -1] = data.ix[i, -1].replace("\\n", "\n")
    data.ix[i, 'Anon Student Id'] = new_id-1

map_student = pd.DataFrame(map_student)
map_student.to_pickle("data/fall2017-fixed/map_student.pkl")
data.to_pickle("data/fall2017-fixed/AllData.pkl")

