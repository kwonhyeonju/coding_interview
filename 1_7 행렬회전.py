''' 행렬회전 : 이미지를 표현하는 N X N 행렬이 있다. 이미지의 각 픽셀은 4바이트로 표현된다. 이때, 이미지를 90도 회전시키는 메서드를 작성하라. 행렬을 추가로 사용하지 않고서도 할 수 있겠는가? '''

data = [[11, 12, 13, 14],
        [21, 22, 23, 24],
        [31, 32, 33, 34],
        [41, 42, 43, 44]]
print("\n< 돌리기 전 행렬 >", data, sep='\n')
print()


def rotate(matrix):
    N = len(data)  # 4
    top = [data[0][i] for i in range(N - 1)]
    # top = data[0][0:N-1] 이렇게 top만 가능
    # 오름차순 말고 내림차순으로 계산할 수 있는 방법이 없을까
    left = [data[i][0] for i in range(1, N)]
    right = [data[i][N-1] for i in range(N-1)]
    bottom = [data[N-1][i] for i in range(1, N)]
    center = [[data[i][j] for j in range(1, N-1)] for i in range(1, N-1)]
    '''
    print("top: ", top, "left: ", left, "right: ",
          right, "bottom: ", bottom, "center: ", center, sep='\n')
    print()'''

    cnt = N-2                           # cnt = 2
    for i in range(N-1):                # N = 4 // i = 0,1,2,3
        # top->right
        cash = right[i]
        right[i] = top[i]
        # left->top
        top[i] = left[cnt]
        # bottom->left
        left[cnt] = bottom[cnt]
        # right->bottom
        bottom[cnt] = cash              # cash = right[i]

        cnt -= 1
    '''print("top: ", top, "left: ", left, "right: ",
          right, "bottom: ", bottom, sep='\n')'''

    # 합치는 방법이 요게 최선일까...
    change_matrix = []

    top.append(right[0])
    center[0].insert(0, left[0])
    center[0].append(right[1])
    center[1].insert(0, left[1])
    center[1].append(right[2])
    bottom.insert(0, left[2])

    change_matrix.append(top)
    change_matrix.append(center[0])
    change_matrix.append(center[1])
    change_matrix.append(bottom)

    # print(change_matrix)
    print("< 90도 돌린 행렬 >")
    return change_matrix


print(rotate(data))
