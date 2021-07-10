from read import get_steps_list
from save import save_texts_in_table

def main():
    """
    Main function
    """
    file_name = "scl.txt"
    steps_list = get_steps_list(file_name)
    table_name = "auto_texts.xlsx"
    save_texts_in_table(table_name, steps_list)


if __name__ == "__main__":
    main()
