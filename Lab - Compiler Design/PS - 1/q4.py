def read():
    try:
        path = 'Macro.c'
        with open(path, 'r') as f:
            fc = f.readlines()  
        evaluate(fc, path)
    except IOError as e:
        print(f'Error: Unable to read file {path} {e}')

def evaluate(fc, path):
    macros = {}
    expanded_code = []

    for line in fc:
        stripped_line = line.strip()
        if stripped_line.startswith('#define'):
            parts = stripped_line.split(maxsplit=2)
            if len(parts) == 3:
                macro_name = parts[1]
                macro_value = parts[2]
                macros[macro_name] = macro_value
                expanded_code.append(line)  
        else:
            # Replace macro calls in the code
            line = expand_macros(line, macros)
            expanded_code.append(line)

    print("Expanded Source Code:")
    for line in expanded_code:
        print(line, end="")

    try:
        wpath = 'ExpandedMacro.c'
        with open(wpath, 'w') as f:
            f.writelines(expanded_code)
        print(f"\nExpanded source code written to {wpath}")
    except IOError as e:
        print(f'Error: Unable to write to file {wpath}\n{e}')

def expand_macros(line, macros):
    for macro_name, macro_value in macros.items():
        if '(' in macro_name and ')' in macro_name:  
            base_name = macro_name[:macro_name.index('(')]
            if base_name in line:
                param = macro_name[macro_name.index('(')+1:macro_name.index(')')]
                param_value = extract_param_value(line, base_name)
                if param_value:
                    macro_expansion = macro_value.replace(param, param_value)
                    macro_expansion = expand_macros(macro_expansion, macros) 
                    line = line.replace(f"{base_name}({param_value})", macro_expansion)
        else:
            line = line.replace(macro_name, macro_value)
    return line

def extract_param_value(line, macro_name):
    start = line.find(f"{macro_name}(")
    if start != -1:
        start += len(macro_name) + 1
        end = line.find(')', start)
        return line[start:end].strip() if end != -1 else None
    return None

read()
