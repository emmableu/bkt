from datetime import datetime
import pandas as pd
homeworkname = 'squiralHW'
#

for student_num in range(0, 26):
    # student_num = 0
    filename = 'generated-data/label2/' + homeworkname + '/student' + str(student_num) + '-' + homeworkname + '.csv'
    new_filename = 'generated-data/label3/' + homeworkname + '/student' + str(student_num) + '-' + homeworkname + '.csv'
    try:
        labels = pd.read_csv(filename, index_col=0)
    except:
        print('not found')
        continue
    start_row = labels.ix[0, 'Row']
    start_time = datetime.strptime(data.ix[start_row, 'Time'], '%Y-%m-%d %H:%M:%S')
    labels.ix[0, 'Timespent'] = 0
    for i in range(1, len(labels.index)):
        row = labels.ix[i, 'Row']
        time = datetime.strptime(data.ix[row, 'Time'], '%Y-%m-%d %H:%M:%S')
        time_spent = (time - start_time).total_seconds()
        labels.ix[i, 'Timespent'] = time_spent
    labels.to_csv(new_filename)




col_names  = ['time2FirstUse', 'time2Success', 'squiralSuccess', 'squiralSuccessBySide', 'squiralFailureByVariable']
labels = pd.DataFrame(columns = col_names)

for student_num in range(0, 26):
    # student_num = 0
    if student_num == 12 or student_num == 20:
        continue
    homeworkname = 'polygonMakerLab'
    p_file = 'generated-data/label3/' + homeworkname + '/student' + str(student_num) + '-' + homeworkname + '.csv'
    p_labels = pd.read_csv(p_file, index_col=0)
    homeworkname = 'squiralHW'
    s_file = 'generated-data/label3/' + homeworkname + '/student' + str(student_num) + '-' + homeworkname + '.csv'
    s_labels = pd.read_csv(s_file, index_col=0)


    for i in range(len(labels.index)):
        if labels.ix[i, 'Row'] == row:
            print("Row exist")
            return
    col_names = ['time2FirstUse', 'time2Success', 'squiralSuccess', 'squiralSuccessBySide', 'squiralFailureByVariable']
    report = ({'Totaltime': totaltime,
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


    try:
        labels = pd.read_csv(new_filename, index_col=0)
    except:
        print('not found')
        continue
    end_time = labels.ix[len(labels.index)-2, 'Timespent']
    print(end_time)


student_num = 25
homeworkname = 'polygonMakerLab'
p_file = 'generated-data/label3/' + homeworkname + '/student' + str(student_num) + '-' + homeworkname + '.csv'
p_labels = pd.read_csv(p_file, index_col=0)
homeworkname = 'squiralHW'
s_file = 'generated-data/label3/' + homeworkname + '/student' + str(student_num) + '-' + homeworkname + '.csv'
s_labels = pd.read_csv(s_file, index_col=0)
