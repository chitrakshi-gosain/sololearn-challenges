import os
import fileinput
from glob import glob
from functools import reduce
from datetime import date
from re import sub


def change_case(filename):
    return reduce(
        lambda x, y: x + ("_" if y.isupper() else "") + y, filename
    ).casefold()


def create_files(filename):
    with open("README.md", "w", encoding="utf-8") as md_file_pointer:
        pass
    md_file_pointer.close()
    with open(f"{change_case(filename)}.py", "w", encoding="utf-8") as py_file_pointer:
        pass
    py_file_pointer.close()


def create_directory(difficulty, directory):
    os.chdir(f".\\{difficulty}")
    path = os.path.join(os.getcwd(), directory)
    os.makedirs(path)
    os.chdir(f".\\{directory}")
    create_files(directory)


if __name__ == "__main__":
    # // add prompts - difficulty levels, diretory name should be camel case
    print(
        "Description:\n This python script creates a directory for you to add your solution for a \
coding challenge to it.\n This solution can be added to the created python file.\n To add a \
prompt describing the problem, a README.md is provided as well.\n\nUsage:\n Difficulty Level:\n   \
Specifies the difficulty of your coding challenge, this helps categorise the challenges easily.\n  \
 You can choose from the following categories: Easy / Medium / Hard\n   These categories are \
case-insensitive :)\n Coding Challenge:\n   This name will be used to create the directory for the \
coding challenge, and it's corresponding files.\n   It is recommended that this field is entered \
in PascalCase for the best results.\n\n\nPlease provide the following details to initialise a \
directory for your new coding challenge:"
    )
    root_addr = os.getcwd()
    difficulty_dir, directory_input = input("Difficulty Level: ").casefold(), input(
        "Coding Challenge: "
    )
    directory_name = sub("[^a-zA-Z]+", "", directory_input)
    difficulty_levels = [level.replace("\\", "").casefold() for level in glob("*/")]
    if difficulty_dir in difficulty_levels:
        create_directory(difficulty_dir, directory_name)
        marker = f" >> {difficulty_dir}"
        description = f"| [{directory_input}]({difficulty_dir.title()}/{directory_name}/README.md)"
        py_soln = f"""| [{directory_name}.py]({difficulty_dir.title()}/{directory_name}/\
{change_case(directory_name)}.py)"""
        date = f'| {date.today().strftime("%b %d, %Y")} |'
        with fileinput.FileInput(f"{root_addr}\\README.md", inplace=True) as f_in:
            for line in f_in:
                print(
                    line.replace(marker, f"\n{description}{py_soln}{date}{marker}"),
                    end="",
                )
        f_in.close()
    else:
        print(
            "Challenges are sorted based on their difficulty levels viz. Easy, Medium, Hard"
        )
