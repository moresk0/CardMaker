# import pyodbc
# cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                       "Server=.;"
#                       "Database=SCANServices-INA-RI-VP;"
#                       "Trusted_Connection=yes;")
#
#
# cursor = cnxn.cursor()
# cursor.execute('SELECT itemName, intval FROM s7tags where (intval is not null and intval != 0)')
#
# for row in cursor:
#     print('row = %r' % (row,))

import pyodbc
import pandas as pd
import numpy as np


cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=.;"
                      "Database=SCANServices-INA-RI-VP;"
                      "Trusted_Connection=yes;")

df = pd.read_sql_query('select intval from s7tags where intval is not null and intval > 0', cnxn)
print(df)













# print(round(np.average(df), 2))
# print(time.ctime())

# while True:
#     if (pyodbc.Error == True):
#         print('Greska')
#     else:
#         print('Ok')
#     time.sleep(1)

# def do_something():
#     print(time.ctime())
# schedule.every(2).seconds.do(do_something)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
