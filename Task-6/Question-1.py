import re

inp_file = open("Task-6\onelinefile.txt", "r")
out_file = open("Task-6\Filename2.csv", "w")

re_int = re.compile(r'\d+')
re_string = re.compile(r'[a-zA-Z]+')
re_float = re.compile(r'\d+\.\d+')

# The required pattern is:
re_pattern = re.compile(r'\d+[a-zA-Z]+[+-]?\d+\.\d+[a-zA-Z]+')
matchSearch = re_pattern.findall(inp_file.read())

# Now we need to insert comma's between the elements
for element in matchSearch:
    int_string = re_int.findall(element)
    string_string = re_string.findall(element)
    float_string = re_float.findall(element)

    element = int_string[0] + "," + string_string[0] + "," + float_string[0] + "," + string_string[1] + "\n"
    out_file.write(element)

inp_file.close()
out_file.close()