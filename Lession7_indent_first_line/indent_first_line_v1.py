def indent_first_line(input_text):
    # lines = [line.strip() for line in input_text]
    lines = input_text.splitlines()
    print(f"lines:\n{lines}")
    new_line = []
    for line in lines:
        line = '    ' + line
        new_line.append(line)
    
    print(f"new_line:\n{new_line}")
    new_text = '\n'.join(new_line)
    print(f"new_text:\n{new_text}")
    return new_text

def main():
    with open('input.txt', 'r', encoding='utf-8') as file:
        # input_text = file.readlines()
        input_text = file.read()
    print(f"input_text:\n{input_text}")
    output_text = indent_first_line(input_text)
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(output_text)

if __name__ == '__main__':
    main()