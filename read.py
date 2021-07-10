from re import compile


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
