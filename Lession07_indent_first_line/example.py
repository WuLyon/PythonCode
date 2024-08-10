def indent_first_line(text):
    """将文本的首行缩进两个空格。"""
    # 将文本按行分割
    lines = text.splitlines()
    
    # 对第一行添加两个空格缩进
    if lines:
        lines[0] = "  " + lines[0]
    
    # 重新合并为单个字符串
    indented_text = "\n".join(lines)
    print(f"indented_text: {indented_text}")
    return indented_text

# 从 input.txt 文件读取文本
with open("input.txt", "r", encoding="utf-8") as input_file:
    input_text = input_file.read()

# 调用函数并获取结果
result = indent_first_line(input_text)

# 将结果保存到 output.txt 文件
with open("output.txt", "w", encoding="utf-8") as output_file:
    print(f"result: {result}")
    output_file.write(result)

print("结果已保存到 output.txt")
