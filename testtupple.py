import ast

string = "(255,0,0)"
color_tuple = ast.literal_eval(string)
print(type(color_tuple))  # Output: (255, 0, 0)
