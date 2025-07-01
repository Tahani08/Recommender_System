'''
@author: Tahani Hassan
'''

def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    file = open ("data/books.txt", "r")

    items = []
    ratings = {}

    for line in file:
        list = line.strip().split(",")

        for i in range(len(list)):
            if i ==0:
                ratings[list[i]] = []
            elif i % 2 != 0:
                if list[i] not in items:
                    items.append(list[i])
            else:
                ratings[list[0]].append(int(list[i]))

    return items, ratings
pass