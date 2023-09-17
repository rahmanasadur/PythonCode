def swap(lst):

    lst = [1,2,3,4,5]
    first = lst.pop(0)   
    last = lst.pop(-1) 
    lst.insert(0, last) 
    lst.append(first)
    return lst

lst=[1,2,3,4,5]
nlst = swap(lst)
print(nlst)
