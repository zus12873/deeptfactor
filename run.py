import os
import subprocess

# 指定文件夹路径
folder_path = "data"

# 获取所有文件（包括子文件夹）
all_files = os.listdir(folder_path)

fasta_files = [os.path.join(folder_path, f) for f in all_files if f.endswith('.fasta')]
# 打印所有的 .fasta 文件
for fasta_file in fasta_files:
    print(fasta_file)
    command = ['python', 'tf_running.py', '-i', f'./{fasta_file}', '-o', './result', '-g', 'cpu']


    subprocess.run(command)
        

