try:
    file_name = input("Enter the file name: ")

    with open(file_name, 'r') as file:
        for line in file:
            print(line.upper(), end='')

except FileNotFoundError:
    print("error occurred no file found")
