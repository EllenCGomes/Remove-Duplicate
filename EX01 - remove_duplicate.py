def remove_duplicates(list):
    list2 = []
    for item in list:
        if not item in list2:
            list2.append(item)
    list.sort(list2)  
    return(list2)