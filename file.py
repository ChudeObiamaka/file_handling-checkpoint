
file_path = r'C:\Users\hp\Desktop\Gomycode Python Class\president_heights_party.csv'

# Opening and printing the entire content of the file
with open(file_path, 'r') as file:
    print(file.read())

# Opening and printing the last line of the file
with open(file_path, 'r') as file:
    last_line = file.readlines()[-1]
    print(last_line)

# Opening and printing the first line of the file
with open(file_path, 'r') as file:
    first_line = file.readlines()[0]
    print(first_line)
