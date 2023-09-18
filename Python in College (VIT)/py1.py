def func(list1):
    while(len(list1) > 2):
        k = list1[0]
        for i in list1:
            if k<i:
                k=i
        list1.remove(k)

        j = list1[0]
        for i in list1:
            if j>i:
                j=i
        list1.remove(j)
    return list1

list2 = func([1,4,3,6,5,3,7,8,9,4])
print(sum(list2)/len(list2))


