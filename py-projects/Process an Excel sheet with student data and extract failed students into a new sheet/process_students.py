import pandas as pd  

input_file = "students.xlsx"         
output_file = "failed_students.xlsx" 
pass_mark = 40                       

# Reading the Excel file into a DataFrame 
students = pd.read_excel(input_file)

# Finding the students who scored less than pass mark
failed_students = students[students["Score"] < pass_mark]

# Showing failed students 
print("Failed students:\n", failed_students)

# Saving failed students to a new Excel file
failed_students.to_excel(output_file, index=False)

print("Saved failed students to", output_file)
