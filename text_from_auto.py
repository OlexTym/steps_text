from openpyxl import Workbook
from re import compile
from re import search


def main():
    """
    Main function
    """
    file_name = "scl.txt"
    steps_list = get_steps_list(file_name)
    table_name = "auto_texts.xlsx"
    save_texts_in_table(table_name, steps_list)


def save_texts_in_table(table_name, steps_list):
    """
    Write steps number and steps comments into xscel table.

    table_name: xscel table name as string
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


def get_steps_list(file_name):
    """
    Return list of lines with steps numbers.

    For ex.:
    '15: // Transportrollen Motor aus'

    file_name: text file in the same dir as string
    """
    with open(file_name, 'r', encoding="utf-8") as file:
        # Find out "CASE*OF"
        raw_line_list = file.readlines()
        start_stop = []
        for line_number, line in enumerate(raw_line_list):
            if "CASE" in line:
                start_stop.append(line_number)

    clear_line_list = raw_line_list[start_stop[0] + 1:start_stop[1]]

    # Find Step number
    steps_list = []
    rgx_step_number = compile(r'[0-9999]:')
    rgx_step_constante = compile(r'#C_STEP[^""]*:')

    for line in clear_line_list:
        if rgx_step_number.search(line) or rgx_step_constante.search(line):
            steps_list.append(line)

    return steps_list


main()
