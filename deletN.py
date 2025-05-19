# 定义文件路径
input_file = "3.txt"  # 原文件路径
output_file = "3_processed.txt"  # 生成的新文件路径

# 读取文件并去除 "\n" 符号
with open(input_file, "r", encoding="utf-8") as infile:
    content = infile.read().replace("\\n", "")  # 删除 \n 符号

# 写入新文件
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write(content)

print(f"处理完成，新文件已保存为：{output_file}")

# 定义输入和输出文件路径
input_file = "原文件.txt"  # 替换为你的原文件路径
output_file = "新文件.txt"  # 替换为你想保存的新文件路径

# 读取文件内容并删除 \n 符号
with open(input_file, "r", encoding="utf-8") as infile:
    content = infile.read().replace("\n", "")

# 将修改后的内容写入新文件
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write(content)

print(f"处理完成，新文件已保存为：{output_file}")



