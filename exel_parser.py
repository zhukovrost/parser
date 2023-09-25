import mysql.connector
from colorama import Fore
import xlrd


def print_error(text):
    print(Fore.RED + text + Fore.GREEN)


cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='english')

cursor = cnx.cursor()

sql = "TRUNCATE TABLE words"
try:
    cursor.execute(sql)
    cnx.commit()
    print("SUCCESSFUL TRUNCATION")
except:
    print_error("ERROR TRUNCATION!")

sql = "INSERT INTO words (word, translate) VALUES (%s, %s)"

workbook = xlrd.open_workbook("words.xlsx")
worksheet = workbook.sheet_by_index(0)
for i in range(2, 270):
    key = worksheet.cell_value(i, 0)
    value = worksheet.cell_value(i, 1)
    sql_values = (key, value)
    try:
        cursor.execute(sql, sql_values)
        cnx.commit()
        print(f"SUCCESSFUL INSERT QUESTION NUMBER {i - 1}!")
    except:
        print_error(f"ERROR INSERTING QUESTION NUMBER {i - 1}!")

