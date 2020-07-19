def validate_Subsequence(array,sequence):
    arrIdx=0
    seqIdx=0
    while(arrIdx<len(array) and seqIdx<len(sequence)):
        if(array[arrIdx]==sequence[seqIdx]):
            seqIdx+=1
        arrIdx+=1
    return seqIdx==len(sequence)
array=[1,2,5,6,-1,10]
sequence=[1,6,10]
print(validate_Subsequence(array,sequence))
