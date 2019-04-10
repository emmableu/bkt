from datetime import datetime
import pandas as pd
a = datetime.strptime('2017-08-29 08:31:05', '%Y-%m-%d %H:%M:%S')
b = datetime.strptime('2017-08-29 09:31:06', '%Y-%m-%d %H:%M:%S')
(b-a).total_seconds()

for student_num in range(0, 26):
    filename = 'generated-data/label2/squiralHW/student' + str(student_num) + '-squiralHW.csv'
    try:
        labels = pd.read_csv('generated-data/label2/student19-polygonMakerLab.csv', index_col= 0)
    except:
        continue
    start_row = labels.ix[0, 'Row']
    start_time =  datetime.strptime(data.ix[start_row, 'Time'], '%Y-%m-%d %H:%M:%S')
    labels.ix[0, 'Timespent'] = 0
    for i in range(1, len(labels.index)):
        row = labels.ix[i, 'Row']
        time = datetime.strptime(data.ix[row, 'Time'], '%Y-%m-%d %H:%M:%S')
        time_spent = (time-start_time).total_seconds()
        labels.ix[i, 'Timespent'] = time_spent
    