a= input("Enter text to write in the file:  ")
file1 = open('C:\GENAI\python_program_pycharm\pythonPycharm_problems\output.txt', 'w')
writing_file = file1.write(a)
print("Data Successfully written to the output.txt")
file1.close()

b= input("Enter text to Append in the file:  ")
file1 = open('C:\GENAI\python_program_pycharm\pythonPycharm_problems\output.txt', 'a')
Appending_file = file1.write('\n' + b)
print("Data Successfully Appended  to the output.txt")
file1.close()


file1 = open('C:\GENAI\python_program_pycharm\pythonPycharm_problems\output.txt', 'r')
reading_file = file1.read()
print(reading_file)
file1.close()

