def remove_comments(input_file, output_file):
    try:
        with open(input_file, "r") as fin, open(output_file, "w") as fout:
            in_multiline_comment = False  
            for line in fin:
                i = 0
                new_line = ""
                while i < len(line):

                    if i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*' and not in_multiline_comment:
                        in_multiline_comment = True
                        i += 1  

                    elif i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/' and in_multiline_comment:
                        in_multiline_comment = False
                        i += 1  

                    elif i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/' and not in_multiline_comment:
                        break  

                    elif not in_multiline_comment:
                        new_line += line[i]
                    i += 1

                if not in_multiline_comment:
                    fout.write(new_line.rstrip() + "\n")
    except IOError:
        print(f"Error: Unable to open file {input_file} or {output_file}.")

input_file = "withComments.cpp"  
output_file = "removeComments.cpp"  
remove_comments(input_file, output_file)

print(f"Comments removed. Cleaned code written to {output_file}.")