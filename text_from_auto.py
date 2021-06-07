from openpyxl import Workbook
from re import compile
from re import search


def step_number(line):
    # '        0: // Init\n'
    number = search('\d+', line)
    return number.group(0) if number else 'none'


def step_comment(line):
    # '        0: // Init\n'
    return (line[line.find('/') + 3: line.find('\n')])


with open('scl.txt', 'r', encoding="utf-8") as file:
    # Find out "CASE*OF"
    raw_line_list = file.readlines()
    start_stop = []
    for line_number, line in enumerate(raw_line_list):  
        if "CASE" in line:
            start_stop.append(line_number)

    clear_line_list = raw_line_list[start_stop[0] + 1:start_stop[1]] 


# Find Step number
steps_list = []
rgx_number = compile(r'[0-9999]:')
rgx_const = compile(r'#C_STEP[^""]*:')

for line in clear_line_list:
    if rgx_number.search(line) or rgx_const.search(line):
        steps_list.append(line)


def main():
    """
    Main function
    """
    table_name = "auto_texts.xlsx"
    save_texts_in_table(table_name, steps_list)


def save_texts_in_table(table_name, steps_list):
    """
    Function to write steps number and steps comment into xscel table.

    :param table_name: xscel table name as string
    :param steps_list: list steps lines with comments
    """
    table = Workbook()
    sheet = table.active

    for i, line in enumerate(steps_list):
        try:
            sheet['A' + str(i+1)] = int(step_number(line))
        except ValueError:
            sheet['A' + str(i+1)] = step_number(line)
        
        sheet['B' + str(i+1)] = step_comment(line)

    table.save(table_name)
    table.close()


main()
