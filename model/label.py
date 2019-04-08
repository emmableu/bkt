import pandas as pd
pd.options.display.max_columns = 30
col_names  = ['Row','Create', 'Use','Pen', 'Repeat', 'Geometry','Cblock','Note']
labels = pd.DataFrame(columns = col_names)
student_num = 17
# labels = pd.read_csv('generated-data/label2/student0-polygonMakerLab.csv', index_col= 0)
filename = 'generated-data/label2/student' + str(student_num) + '-polygonMakerLab.csv'
def fill_labels(row, create, use, pen, repeat, geometry, cblock, note):
    global labels
    for i in range(len(labels.index)):
        if labels.ix[i, 'Row'] == row:
            print("Row exist")
            return
    new_record = ({'Row': row,
                    'Create': create,
                   'Use': use,
                   'Pen': pen,
                   'Repeat':repeat,
                   'Geometry': geometry,
                   'Cblock':cblock,
                    'Note':note})
    labels.loc[len(labels)] = new_record
    # labels = labels.append(new_record, ignore_index = True)
    labels = labels.sort_values(['Row']).reset_index(drop=True)
    labels.to_csv(filename)
    print(labels)


def change_labels(row, create, use, pen, repeat, geometry, cblock, note):
    global labels
    new_record = ({'Row': row,
                    'Create': create,
                   'Use': use,
                   'Pen': pen,
                   'Repeat':repeat,
                   'Geometry': geometry,
                   'Cblock': cblock,
                    'Note':note})
    for i in range(len(labels.index)):
        if labels.ix[i, 'Row'] == row:
            labels.loc[i] = new_record
    labels = labels.sort_values(['Row']).reset_index(drop=True)
    labels.to_csv(filename)
    print(labels)


def delete_label(row):
    global labels
    for i in range(len(labels.index)):
        if labels.ix[i, 'Row'] == row:
            labels = labels.drop(labels.index[i])
    labels = labels.sort_values(['Row']).reset_index(drop=True)
    labels.to_csv(filename)
    print(labels)



fill_labels(row = 49041, create =3, use = 4, pen = 3, repeat =6, geometry = 3, cblock = 1, note = '         turn(!!!!!reportQuotient(literal=360, var=sides))')
# delete_label(48821)
#
print(labels)


labels['Anon Student Id'] = map_student.ix[student_num,  'Anon Student Id']
labels['New Id'] = student_num
labels.to_csv(filename)
# labels = pd.read_csv('generated-data/label2/student0-polygonMakerLab.csv')
for i in range(4, 7):
    labels.ix[i, 'Create'] =2

# fill_labels(row = 284, create = 0, use = 0, pen = 0, repeat = 0, geometry = 0, cblock = 0, note = "codestart")

