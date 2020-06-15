def matrixDotProduct(matrixA,matrixB):
    #ここから書きましょう
    answer_list =[]
    matrixA_list = side_line(matrixA)
    matrixB_list = vertical_line(matrixB)
    for i in range(0,int(len(matrixA)**0.5)):
        for j in range(0,int(len(matrixA)**0.5)):
            innner_num = 0
            for k in range(0,int(len(matrixA)**0.5)):
                innner_num += (matrixA_list[i][k]*matrixB_list[j][k])
            else:
                answer_list.append(innner_num)

    return answer_list

def side_line(matrix):

    side_line = [matrix[i:i+int(len(matrix)**0.5)] for i in range(0,int(len(matrix)),int(len(matrix)**0.5))]
    return side_line

def vertical_line(matrix):
    vertical_line = []
    vertical = [matrix[i:i + int(len(matrix) ** 0.5)] for i in range(0, int(len(matrix)), int(len(matrix) ** 0.5))]
    for i in range(0,int(len(matrix)**0.5)):
        vertical_base = []
        for j in range(0,int(len(matrix)**0.5)):
            vertical_base.append(vertical[j][i])
        else:
            vertical_line.append(vertical_base)
    return vertical_line

print(matrixDotProduct([1,2,3,4],[5,6,7,8]))