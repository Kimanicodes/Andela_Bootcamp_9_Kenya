def dupli(A):
    temp = []
    for i in range(0, len(A) - 1):
        if A[i] != A[i + 1]:
            temp.append(A[i])
    temp.append(A[len(A) - 1])
    return temp


#Testing the function
print(dupli([5, 5, 6, 6 ,10, 7, 5]))
