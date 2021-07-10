from openpyxl import Workbook
from re import search


def save_texts_in_table(table_name, steps_list):
    """
    Write steps number and steps comments into xcel table.

    table_name: xcel table name as string
    steps_list: list of steps lines with comments
    """
    table = Workbook()
    sheet = table.active

    for i, line in enumerate(steps_list):
        try:
            sheet['A' + str(i+1)] = int(get_step_number(line))
        except ValueError:
            sheet['A' + str(i+1)] = get_step_number(line)

        sheet['B' + str(i+1)] = get_step_comment(line)
    table.save(table_name)
    table.close()


def get_step_number(line):
    # '        0: // Init\n'
    number = search('\d+', line)
    return number.group(0) if number else 'none'


def get_step_comment(line):
    # '        0: // Init\n'
    return (line[line.find('/') + 3: line.find('\n')])