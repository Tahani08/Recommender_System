'''
@author: Tahani Hassan
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''
    items = set()
    ratings = {}

    with open("data/movies.txt", "r") as file:
        for line in file:
            user, item, rating = line.strip().split(',')
            rating = int(rating)
            items.add(item)
            if user not in ratings:
                ratings[user] = {}
            ratings[user][item] = rating

    items = sorted(items)
    ratings_dict = {}
    for user in ratings:
        ratings_dict[user] = []
        for item in items:
            if item in ratings[user]:
                ratings_dict[user].append(ratings[user][item])
            else:
                ratings_dict[user].append(0)
    return items, ratings_dict
    pass