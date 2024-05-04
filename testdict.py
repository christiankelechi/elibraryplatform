import ast

string = "{'status':True,'message':'Message successful'}"
color_tuple = ast.literal_eval(string)
print(color_tuple)
print(type(color_tuple))  # Output: (255, 0, 0)
