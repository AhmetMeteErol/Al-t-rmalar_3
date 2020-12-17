def QuickSort(list4input):
    if len(list4input) == 0 or len(list4input) == 1:
        return list4input

    else:
        index_pivot = len(list4input)//2                            # We select our pivot as middle number
        LeftList = []                                               # The smaller numbers go to left list
        RightList = []                                              # The bigger numbers go to right list
        
        for i in range(0,len(list4input)):
            if list4input[i] < list4input[index_pivot]:
                LeftList.append(list4input[i])                      # We add small ones to left list
            elif list4input[i] > list4input[index_pivot]:
                RightList.append(list4input[i])
        
    
    return QuickSort(LeftList) + [list4input[index_pivot]] + QuickSort(RightList)        # We recall our function recursively for left and right lists
    
    

a = [1,3, 2, 5, 4,7,10,0]
print(QuickSort(a))