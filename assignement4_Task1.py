try:
    file1 = open('C:\GENAI\python_program_pycharm\pythonPycharm_problems\simple.txt' , 'r')
    reading_file = file1.read()
    print(reading_file)
    file1.close()
except FileNotFoundError:
        print("Error: The file 'Simple.txt' not found ")

