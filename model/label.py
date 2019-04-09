import pandas as pd
pd.options.display.max_columns = 30
col_names  = ['Row','Pcreate', 'Puse','Vcreate', 'Vuse','Update', 'Pen', 'Repeat', 'Geometry','Cblock','Note']
labels = pd.DataFrame(columns = col_names)
student_num = 11
# labels = pd.read_csv('generated-data/label2/student19-polygonMakerLab.csv', index_col= 0)
filename = 'generated-data/label2/squiralHW/student' + str(student_num) + '-squiralHW.csv'
def fill_labels(row, pcreate, puse, vcreate, vuse, update, pen, repeat, geometry, cblock, note):
    global labels
    for i in range(len(labels.index)):
        if labels.ix[i, 'Row'] == row:
            print("Row exist")
            return
    new_record = ({'Row': row,
                    'Pcreate': pcreate,
                   'Puse': puse,
                   'Vcreate': vcreate,
                   'Vuse': vuse,
                   'Update': update,
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


def change_labels(row, pcreate, puse, vcreate, vuse, update, pen, repeat, geometry, cblock, note):
    global labels
    new_record = ({'Row': row,
                    'Pcreate': pcreate,
                   'Puse': puse,
                   'Vcreate': vcreate,
                   'Vuse': vuse,
                   'Update': update,
                   'Pen': pen,
                   'Repeat':repeat,
                   'Geometry': geometry,
                   'Cblock':cblock,
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



fill_labels(row = 36937,
            pcreate = 0, puse = 0,
            vcreate = 0,  vuse = 0, update = 1,
            pen = 0, repeat = 0,
            geometry = 0, cblock = 0,
            note = ' code start')

# fill_labels(row = 31515,
#             pcreate = 2, puse = 2,
#             vcreate = 0,  vuse = 0, update = 0,
#             pen = 1, repeat = 3,
#             geometry = 0, cblock = 1,
#             note = '     forward([!!!!!var=Size])')
#



delete_label(79521)
#
print(labels)

labels['Anon Student Id'] = map_student.ix[student_num,  'Anon Student Id']
labels['New Id'] = student_num
labels.to_csv(filename)
# labels = pd.read_csv('generated-data/label2/student0-polygonMakerLab.csv')
for i in range(13, 15):
    labels.ix[9, 'Pen'] =1

# fill_labels(row = 284, create = 0, use = 0, pen = 0, repeat = 0, geometry = 0, cblock = 0, note = "codestart")

