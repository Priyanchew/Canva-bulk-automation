import re
import pandas as pd

df = pd.read_excel('excel.xlsx')
# Function to remove text within parentheses or brackets
def remove_text_in_brackets(s):
    return re.sub(r'\[.*?\]|\(.*?\)', '', s).strip()

# Process each string in the list
processed_strings = [remove_text_in_brackets(s) for s in df['NAME']]

list_of_names = []

# Print the processed strings
for string in processed_strings:
    x = string.title()
    list_of_names.append(x)
print(list_of_names)



