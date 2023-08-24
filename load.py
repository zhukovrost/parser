import mysql.connector
from json import load, dumps
from colorama import Fore


def print_error(text):
    print(Fore.RED + text + Fore.GREEN)

# --------------- preparing ---------------------


print(Fore.GREEN)

cnx = mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='english')

cursor = cnx.cursor()

truncate_sqls = ["TRUNCATE TABLE questions", "TRUNCATE TABLE tests", "TRUNCATE TABLE themes"]
for sql in truncate_sqls:
    try:
        cursor.execute(sql)
        cnx.commit()
        print("SUCCESSFUL TRUNCATION")
    except:
        print_error("ERROR TRUNCATION!")


# --------------- INSERTING THEMES --------------------

with open("themes.json") as f:
    theme_list = load(f)

for theme in theme_list:
    insert_sql = f"INSERT INTO themes (theme) VALUES (%s)"
    # Execute the query
    try:
        cursor.execute(insert_sql, [theme])
        cnx.commit()
        print(f"SUCCESSFUL INSERT THEME {theme}")
    except:
        print_error(f"ERROR INSERTING THEME {theme}")

# --------------- INSERTING QUESTIONS ------------------

with open("questions.json") as f:
    question_list = load(f)

for question in question_list:

    values = (
        question['id'],
        question['question'][0:-1],
        question['theme'],
        question['type'],
        dumps(question['variants']),
        dumps(question['right_answers']),
        question['score'],
        question['image']
    )

    insert_sql = "INSERT INTO questions (id, question, theme, type, variants, right_answers, score, image) " \
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    # Execute the query with the values
    try:
        cursor.execute(insert_sql, values)
        cnx.commit()
        print(f"SUCCESSFUL INSERT QUESTION NUMBER {question['id']}!")
    except:
        print_error(f"ERROR INSERTING QUESTION NUMBER {question['id']}!")


# -------------------- INSERTING TESTS -------------------

with open("tests.json") as f:
    test_list = load(f)

for test in test_list:

    values = (
        test['id'],
        test['name'],
        test['task'],
        dumps(test['test']),
        dumps(test['themes']),
    )

    insert_sql = "INSERT INTO tests (id, name, task, test, themes) VALUES (%s, %s, %s, %s, %s)"

    # Execute the query with the values
    try:
        cursor.execute(insert_sql, values)
        cnx.commit()
        print(f"SUCCESSFUL INSERT TEST NUMBER {test['id']}!")
    except:
        print_error(f"ERROR INSERTING TEST NUMBER {test['id']}!")


# ---------------- STOPPING THE PROGRAM -----------------------

cursor.close()
cnx.close()
