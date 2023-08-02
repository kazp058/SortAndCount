def merge_and_count(A, B):

    pointer_A = 0
    pointer_B = 0

    count = 0
    output = []

    while pointer_A < len(A) and pointer_B < len(B):
        a = A[pointer_A]
        b = B[pointer_B]

        if a <= b:
            output.append(a)
            pointer_A += 1
        elif b < a:
            count += len(A[pointer_A:])
            output.append(b)
            pointer_B += 1
    
    if pointer_A < len(A):
        output = output + A[pointer_A:]
    if pointer_B < len(B):
        output = output + B[pointer_B:]
    
    return count, output

def sort_and_count(L):

    if len(L) == 1:
        return 0, L
    
    else:
        idx_half = round(len(L) / 2)
        A = L[:idx_half] 
        B = L[idx_half:] 

        print(A, B)

        counter_A, A = sort_and_count(A)
        counter_B, B = sort_and_count(B)

        counter_M, L = merge_and_count(A, B)
    
    return counter_A + counter_B + counter_M, L

L1 = [5, 3, 1, 4, 2]
L2 = [2,4,5,3,1]

print(sort_and_count(L1))
print(sort_and_count(L2))