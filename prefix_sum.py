def prefix_sum(array):

    for i in range(1,len(array)):
        array[i]+=array[i-1]
    
    return array

array=list(map(int,input("Enter the Array Elements : ").split()))
print(prefix_sum(array))