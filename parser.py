from json import load, dumps
from pdfquery import PDFQuery
import os

themes_json = open('themes.json', 'r')
themes = load(themes_json)
themes_json.close()

tests = {}

for file in os.scandir('files'):
    path = file.path
    filename = path.replace('files/', '')
    print(filename, end='\n\n')
    pdf = PDFQuery(path)
    pdf.load()
    text_elements = pdf.pq('LTTextBoxHorizontal')

    lines = []
    questions = {}
    for t in text_elements:
        line = t.text
        if '.' in line:
            lines.append(line)

    for question_number in range(1, len(lines) // 2 + 1):
        point = str(question_number) + '.'
        array = []
        for element in range(len(lines)):
            if lines[element].find(point) == 0:
                array.append(lines[element].replace(point + ' ', ''))

        if array != [] or question_number == 1:
            questions[str(question_number)] = array

    tests[filename] = questions

f = open('unformatted_data.json', 'r+')
f.write(dumps(tests))
f.close()

