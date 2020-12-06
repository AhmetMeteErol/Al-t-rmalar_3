# This programme contains a function which sorts
# numbers by using insert sort algorithm

# Algorithm works in this way:
# divide into 2 sublists which are sorted and unsorted lists
# sorted list will have length of one and rest items go to unsorted list
# Then algorithm starts to get items into sorted sublist
# Once item in sorted sublist, we compare them and swap if it's necesarry
 

def insert_sort(myList):
    index_length = len(myList)
    
    for i in range(1,index_length):                                     # sublist starts with 1st index of the list so range func starts with 1
        value_2_sort = myList[i]
            
        while myList[i-1] > value_2_sort and i>0:
            myList[i-1], myList[i] = myList[i], myList[i-1]
            i -= 1                                                      # We increase i for continue to compare 
    
    return myList

print(insert_sort([1,4,2,5,3]))

''' liste = [1,4,2,5,3] index length = 5 
value_2sort is 4 for instance. and we swap with 1 (mylist[0]) while mylist[i-1]> to sort value.'''
