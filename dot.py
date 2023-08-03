import pandas as pd
#这是一个测试文件
# 读取第一个CSV文件（m,5矩阵）
# df1 = pd.read_csv('/Users/geyaogang/Desktop/毕设/computer_by_hand/date_matrix.py')

file1_path = "computer_by_hand/date-matrix.csv"
df1 = pd.read_csv(file1_path, header=None)
# 读取第二个CSV文件
file2_path = "computer_by_hand/weight_matrix.csv"
df2 = pd.read_csv(file2_path, header=None)
# 读取第三个CSV文件
file2_path = "computer_by_hand/weight_matrix.csv"
df2 = pd.read_csv(file2_path, header=None)


# 读取第二个CSV文件（5,1矩阵）
# df2 = pd.read_csv('/Users/geyaogang/Desktop/毕设/computer_by_hand/weight_matrix.csv')

# 进行点乘运算得到(m,1)矩阵
result = df1.dot(df2)

    # 调试输出
print("第一个矩阵:")
print(df1)
print("\n第二个矩阵:")
print(df2)

# 对结果进行标准化，使列元素和为1
normalized_result = result / result.sum()


# 打印标准化后的结果
print(normalized_result)