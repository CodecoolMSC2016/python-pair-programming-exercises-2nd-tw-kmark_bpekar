def listoverlap(list1, list2):
    list3=[]
    for item in list1:
        if item in list2:
           if item not in list3:
               list3.append(item)
    
    return list3


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = listoverlap(a,b)
    print(c)
    return


if __name__ == '__main__':
    main()
