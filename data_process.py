import os

def split_fasta(input_file, batch_size=15, output_dir="output"):
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 读取输入文件中的所有序列
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # 提取序列 ID 和序列数据
    seq_ids = []
    sequences = []
    for i in range(0, len(lines), 2):  # 假设每个序列由两行组成：ID 行和序列行
        seq_ids.append(lines[i].strip())
        sequences.append(lines[i + 1].strip())

    # 确保所有数据都被处理，不遗漏
    total_sequences = len(sequences)
    num_batches = (total_sequences // batch_size) + (1 if total_sequences % batch_size != 0 else 0)

    # 拆分序列，每 batch_size 个样本保存一个文件
    for batch_num in range(num_batches):
        # 计算当前批次的起始和结束索引
        start_idx = batch_num * batch_size
        end_idx = min((batch_num + 1) * batch_size, total_sequences)

        # 生成输出文件名
        output_file = os.path.join(output_dir, f"batch_{batch_num + 1}.fasta")

        # 保存当前批次的序列到文件
        with open(output_file, 'w') as out_f:
            for i in range(start_idx, end_idx):
                out_f.write(f">{seq_ids[i]}\n")
                out_f.write(f"{sequences[i]}\n")

        print(f"Saved batch {batch_num + 1} to {output_file}")

if __name__ == "__main__":
    input_file = "Dataset/cgi_pep.fa"  # 这里替换为你的输入文件路径
    split_fasta(input_file, batch_size=15, output_dir="data")
