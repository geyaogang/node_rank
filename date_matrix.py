import csv
import pandas as pd
import numpy as np

def dot_matrix(matrix1, matrix2):
    # 进行点乘运算得到(m,1)矩阵
    dot_matrix = matrix1.dot(matrix2)
    return dot_matrix

def normalize_columns(matrix):
    # 获取每一列的和
    column_sums = matrix.sum(axis=0)
    # 对每一列进行标准化
    normalized_matrix = matrix / column_sums
    return normalized_matrix    
    # return (matrix - matrix.min()) / (matrix.max() - matrix.min())
    # return (dot_matrix / dot_matrix.sum(axis=0)) 

def write_csv(filename, matrix):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(matrix)

def main():
    # 读取第一个CSV文件  原生数据
    file1_path = "computer_by_hand/raw_date_matrix.csv"
    df1 = pd.read_csv(file1_path, header=None)
    # 读取第二个CSV文件 权重 数据
    file2_path = "computer_by_hand/weight_matrix.csv"
    df2 = pd.read_csv(file2_path, header=None)
    # 读取第三个CSV文件  全1 矩阵
    file3_path = "computer_by_hand/all_one_matrix.csv"
    df3 = pd.read_csv(file3_path, header=None)
    # # 调试输出
    # print("第一个矩阵:")
    # print(df1)
    # print("\n第二个矩阵:")
    # print(df2)

    # 进行点乘运算
    result_matrix = dot_matrix(df1, df2)

    # 对新的矩阵的每一列进行归一化
    normalized_matrix = normalize_columns(result_matrix)
    # #检验是否和为1
    # sum_normalized_matrix = normalized_matrix.sum(axis=0)

    date_matrix = dot_matrix(normalized_matrix,df3)

    # 将矩阵转换为DataFrame对象
    df = pd.DataFrame(date_matrix)
    # 将DataFrame保存为CSV文件
    df.to_csv('/Users/geyaogang/Desktop/毕设/computer_by_hand/data_matrix.csv', index=False, header=None)
    
    # 打印结果
    print("点乘得到的矩阵:")
    print(result_matrix)
    print("\n归一化后的矩阵:")
    print(normalized_matrix)
    # print("\n检验是否和为1:")
    # print(sum_normalized_matrix)
    print("\n数据矩阵:")
    print(date_matrix)

if __name__ == "__main__":
    main()
