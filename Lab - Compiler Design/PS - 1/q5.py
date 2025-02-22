def read():
    try:
        path = 'Macro.c'
        with open(path , 'r') as f:
            fc = f.readlines() 
            evaluate(fc, path)
    
    except IOError as e:
        print(f'Error: while opening the file: {path}\n {e}')
    
def evaluate(fc, path):
    i = 1
    addlineno = []
    for line in fc:
        line = str(i) + ' ' + line
        i += 1
        addlineno.append(line)
    for line in addlineno:
        print(line, end='')
    
    try:
        wpath = 'addLineNo.c'
        with open(wpath, 'w') as f:
            f.writelines(addlineno)
    except IOError as e:
        print(f'Error: while writing to the file: {wpath}\n {e}')

read()