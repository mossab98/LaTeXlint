import argparse
import json
from mailbox import linesep


def main():
    parser = argparse.ArgumentParser(description='Name of LaTeX file')
    parser.add_argument('file_name', type=str, help='Input .tex file name')
    args = parser.parse_args()
    file_name = args.file_name
    
    if file_name.endswith(".tex") is False:
        print("This file is incompatible, insert a compatible LaTeX file")
    else:
        contents_file = read_from_tex(file_name)
        test = read_from_json()
        new_line = test["newline"]
        blank_lines = test["blanklines"]
        blank_lines_true_or_false = blank_lines[0].get("active")
        blank_lines_amount = blank_lines[1].get("amount")

        if new_line == True and blank_lines_true_or_false == True:
            cont_newline = add_lines(contents_file)
            finished_cont = add_blank_lines(cont_newline, blank_lines_amount)
        elif new_line == True and blank_lines_true_or_false == False:
            finished_cont = add_lines(contents_file)
        elif new_line == False and blank_lines_true_or_false == True:
            finished_cont = add_blank_lines(contents_file, blank_lines_amount)
                 
        write_to_tex(finished_cont, file_name)

def read_from_json():
    with open("rules.json", "r") as json_file:
        json_data = json_file.read()
        json_info = json.loads(json_data)
        json_file.close()
        return json_info


def read_from_tex(Input_filename):

    contents = []
    with open(Input_filename , "r+", encoding="utf8") as file:
        contents = file.readlines()
        file.close()
        return contents

def write_to_tex(contents, file):
    modified_file = file + "_lintered.tex"
    modified_file = open(modified_file, "w")
    for line in contents:
        modified_file.writelines(line)
    modified_file.close()
        

def add_lines(contents):
    list_filter = [".", "!", "?"]
    list_new_content = []
    
    for line in contents:
        cnt_letter = 0
        len_str = 0
        for letter in line:
            filter_line = list(filter(letter.startswith, list_filter)) != []
            if filter_line == True:
                new_line = line[len_str:cnt_letter + 1] + "\n"
                len_str = len_str + len(new_line) 
                list_new_content.append(new_line)  
            cnt_letter += 1
        list_new_content.append(line[len_str:])      
    return list_new_content


def add_blank_lines(contents, amount):
    
    list_packages = ["\chapter","\section","\subsection","\subsubsection"]
    list_new_content = []
    for line in contents:
        filter_line = list(filter(line.startswith, list_packages)) != []
        if filter_line == True:
            line = "\n" * amount + line
            list_new_content.append(line)
        else:
            list_new_content.append(line)
    return list_new_content

if __name__ == '__main__':
    main()
    