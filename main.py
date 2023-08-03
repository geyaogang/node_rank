import numpy as np
import csv

# 从CSV文件中读取矩阵数据
def read_matrix_from_csv(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            row = [float(element) for element in row]
            matrix.append(row)
    return np.array(matrix)

# 求三个矩阵的和并返回新的矩阵
def sum_matrices(matrix1, matrix2, matrix3):
    return 0.4 * matrix1 + 0.5 * matrix2 + 0.1 * matrix3

# 求特征值和特征向量并返回结果
def compute_eigen(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

# 读取三个矩阵的数据
matrix1 = read_matrix_from_csv('/Users/geyaogang/Desktop/毕设/computer_by_hand/trans_matrix1.csv')#概率转移矩阵
matrix2 = read_matrix_from_csv('/Users/geyaogang/Desktop/毕设/computer_by_hand/data_matrix.csv')#数据矩阵
matrix3 = read_matrix_from_csv('/Users/geyaogang/Desktop/毕设/computer_by_hand/random_matrix3.csv')#随机矩阵

# 调试输出
print("第一个矩阵:")
print(matrix1)
print("\n第二个矩阵:")
print(matrix2)
print("\n第三个矩阵:")
print(matrix3)

# 计算求和后的新矩阵，并输出结果
sum_matrix = sum_matrices(matrix1, matrix2, matrix3)
print("马尔可夫矩阵:")
print(sum_matrix)

# 计算新矩阵的特征值和特征向量，并输出结果
eigenvalues, eigenvectors = compute_eigen(sum_matrix)

# print("\n特征值:")
# print(eigenvalues)
# print("\n特征向量:")
# print(eigenvectors)

print("\n特征值:", eigenvalues)
print("\n特征向量:")
for i in range(len(eigenvectors)):
    print(eigenvectors[:, i])