from json import load, dumps
from colorama import Fore
from os import remove

# --------- functions ------------


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


# ------------ importing dat from files ---------------

with open("unformatted_data.json") as f1:
    unformatted_data = load(f1)

with open("themes.json") as f2:
    themes = load(f2)

with open("tests.json") as f3:
    tests = load(f3)

with open("questions.json") as f5:
    questions = load(f5)

# ----------- program -------------------

delete_files = set()

if len(unformatted_data) != 0:

    for unformatted_item in unformatted_data.items():

        filename = unformatted_item[0]
        unformatted_test = unformatted_item[1]
        formatted_test = {}

        print(Fore.MAGENTA)
        print(filename, '\n')
        print(Fore.RESET)
        print(f"Here is an example:\nQuestion: {unformatted_test['3'][0]}\nAnswer: {unformatted_test['3'][1]}\n\nChoose the question type:\n1 - One blank field with different possible answers.\n2 - Several blank fields with one answer variant.\n3 - Do not include this test\n4 - Stop the programm\n")
        question_type = int(input("Enter 1 or 2 or 3 or 4: "))

        if question_type == 4:
            break

        if question_type != 3:
            if question_type == 1:
                question_type = "definite"
            elif question_type == 2:
                question_type = "missing_words"

            print_test(unformatted_test)
            ok = int(input("Is this test correct?\n0 - no\n1 - yes\n3: discard changes and continue with the next test\nFill the blank: "))
            if ok != 3:
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

                print(Fore.GREEN)

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
                    with open("questions.json", "r+") as update_question_list_file:
                        update_question_list_file.write(dumps(questions))

                    formatted_test['test'].append(len(questions))

                    print(f"Added new question! ID: {len(questions)}!")

                tests.append(formatted_test)
                with open("tests.json", "r+") as update_test_list_file:
                    update_test_list_file.write((dumps(tests)))

                print(f"Added new test! ID: {formatted_test['id']}")
                print(Fore.RESET)

                delete_files.add(filename)

        print('\n' + Fore.GREEN + 'SUCCESS!\n' + Fore.RESET)


    # ----------- deleting used files ---------------------

    print(Fore.GREEN)

    for filename in delete_files:
        unformatted_data.pop(filename)
        remove("files/" + filename)
        print(f"Successfully deleted unformatted data and file files/{filename}")


    with open("unformatted_data.json", "r+") as update_data_file:
        update_data_file.write(dumps(unformatted_data))

    print("Successfully updated unformatted data file!")

else:
    print(Fore.MAGENTA + "All files are already formatted!" + Fore.RESET)

print(Fore.RED + "Stopping the program..." + Fore.RESET)
