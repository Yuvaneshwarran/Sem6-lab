# Question 3

def read():
    try:
        path = 'sample.txt'
        with open(path, 'r') as f:
            filecontent = f.read()
            evaluate(path)
    except IOError as e:
        print(f"Error reading file: {e}")

def evaluate(path):
    try:
        with open(path, "r") as file:
            alpha = 0
            digit = 0
            space = 0
            specialchars = 0
            lines = 0
            words = 0
            while True:
                char = file.read(1) 
                if char.isalpha():
                    alpha += 1 
                elif char.isdigit():
                    digit += 1
                elif char.isspace():
                    space += 1
                elif not char.isalnum():
                    specialchars += 1
                if not char:         
                    break
            file.seek(0)
            while True:
                line = file.readline()
                if not line:
                    break
                lines += 1
                words += len(line.split(' '))
            print(f"\nTotal Alphabets: {alpha}")
            print(f"Total Digits: {digit}")
            print(f"Total Spaces: {space}")
            print(f"Total Special Characters: {specialchars}")
            print(f"Total Lines: {lines}")
            print(f"Total Words: {words}")
    except IOError:
        print("Error reading file."+ IOError.message)

read()


