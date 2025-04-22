def mergeSort(A, Left, Right):
    if Left < Right:
        Mid = (Right + Left) // 2
        mergeSort(A, Left, Mid)  # lewa
        mergeSort(A, Mid + 1, Right)  # prawa
        merge(A, Left, Right)


def merge(A, Left, Right):
    Mid = (Right + Left) // 2
    Len1 = Mid - Left + 1
    Len2 = Right - Mid
    Left_A = A[Left : Mid + 1]  # Left - Mid
    Right_A = A[Mid + 1 : Right + 1]  # Mid + 1 - Right
    Left_index = Right_index = 0
    Main_index = Left

    while Left_index < Len1 and Right_index < Len2:
        if Left_A[Left_index] <= Right_A[Right_index]:
            A[Main_index] = Left_A[Left_index]
            Left_index += 1
        else:
            A[Main_index] = Right_A[Right_index]
            Right_index += 1
        Main_index += 1

    while Left_index < Len1:
        A[Main_index] = Left_A[Left_index]
        Left_index += 1
        Main_index += 1

    while Right_index < Len2:
        A[Main_index] = Right_A[Right_index]
        Right_index += 1
        Main_index += 1


from random import randint

A = [randint(1, 20) for _ in range(20)]
print(A)
mergeSort(A, 0, len(A) - 1)
print(A)
