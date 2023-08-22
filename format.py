from json import load, dumps
from colorama import Fore, Style


def print_question(test, number):
    print(str(number), ".\nQuestion: ", sep='', end='')

    try:
        print(test[str(number)][0], end='')
    except:
        print(Fore.RED + "NONE!!!")
        print(Fore.RESET)


    print("\nAnswer: ", end='')

    try:
        print(test[str(number)][1], end='')
    except:
        print(Fore.RED + 'NONE!!!')
        print(Fore.RESET)

    print("\n")


def print_test(test):
    print("\n")
    for i in range(1, len(test) + 1):

        print_question(test, i)

    print('\n')


f1 = open("unformatted_data.json")
unformatted_data = load(f1)
f1.close()


f2 = open("themes.json")
themes = load(f2)
f2.close()

excluded = {}
tests = []
questions = []

for unformatted_item in unformatted_data.items():

    filename = unformatted_item[0]
    unformatted_test = unformatted_item[1]
    formatted_test = {}

    print(Fore.MAGENTA)
    print(filename, '\n')
    print(Fore.RESET)
    print("Here is an example:\nQuestion: ", unformatted_test["3"][0], "\nAnswer: ", unformatted_test["3"][1], "\n\nChoose the question type:\n1 - One blank field with different possible answers.\n2 - Several blank fields with one answer variant.\n3 - Do not include this test\n", sep='')
    question_type = int(input("Enter 1 or 2 or 3: "))

    if question_type != 3:
        if question_type == 1:
            question_type = "definite"
        elif question_type == 2:
            question_type = "missing_words"

        print_test(unformatted_test)
        ok = int(input("Is this test correct? 0 - no, 1 - yes: "))

        while ok != 1:
            incorrect_number = input("Enter the question number, which is incorrect: ")
            print_question(unformatted_test, incorrect_number)
            incorrect_option = input("Enter the option:\n1 - Change question.\n2 - Change answer.\n\nLeave the field blank to go back: ")

            while incorrect_option == "1" or incorrect_option == "2":

                if incorrect_option == "1":
                    question = input("Enter new question: ")
                    try:
                        unformatted_test[incorrect_number][0] = question
                    except:
                        unformatted_test[incorrect_number].append(question)

                elif incorrect_option == "2":
                    answer = input("Enter new answer: ")
                    try:
                        unformatted_test[incorrect_number][1] = answer
                    except:
                        unformatted_test[incorrect_number].append(answer)

                print_question(unformatted_test, incorrect_number)
                incorrect_option = input("Enter the option:\n1 - Change question.\n2 - Change answer.\n\nLeave the field blank to go back: ")

            print_test(unformatted_test)
            ok = int(input("Is this test correct? 0 - no, 1 - yes: "))

        name = input("\nEnter the name: ")
        task = input("\nEnter the task / question: ")
        score = input("\nEnter the question score (leave blank = 1): ")
        if score != '':
            score = int(score)
        else:
            score = 1

        for i in range(len(themes)):
            print(i + 1, '. ', themes[i], sep='')

        theme = input("Choose theme (0 - without theme): ")
        if theme.isnumeric():
            theme = int(theme)
        else:
            theme = 0

        formatted_test['id'] = len(tests) + 1
        formatted_test['name'] = name
        formatted_test['task'] = task
        formatted_test['test'] = []
        formatted_test['themes'] = [theme]

        for unformatted_question in unformatted_test.values():
            formatted_question = {}
            formatted_question['id'] = len(questions) + 1
            formatted_question['question'] = unformatted_question[0]
            formatted_question['theme'] = theme
            formatted_question['type'] = question_type
            formatted_question['variants'] = []
            formatted_question['right_answers'] = [unformatted_question[1]]
            formatted_question['score'] = score
            formatted_question['image'] = 0
            questions.append(formatted_question)
            formatted_test['test'].append(len(questions))

        tests.append(formatted_test)

        print(formatted_test)

    else:
        excluded[filename] = unformatted_test

    print('\n' + Fore.GREEN + 'SUCCESS!\n' + Fore.RESET)

f3 = open("excluded.json", "r+")
f3.write(dumps(excluded))
f3.close()

f4 = open("tests.json", "r+")
f4.write(dumps(tests))
f4.close()

f5 = open("questions.json", "r+")
f5.write(dumps(questions))
f5.close()
