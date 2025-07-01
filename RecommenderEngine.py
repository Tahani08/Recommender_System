'''
@author: Tahani Hassan
'''
from typing import final


def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''
    final = []

    for index in range(len(items)):
        item_ratings = []
        for user, user_ratings in ratings.items():
           rating = user_ratings[index]
           if rating != 0:
                item_ratings.append(rating)

        if len(item_ratings) > 0:
            average = sum(item_ratings) / len(item_ratings)
        else:
            average = 0.0

        final.append((items[index], average))

    final.sort(key=lambda x: (-x[1], x[0]))
    return final

def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''
    if name not in ratings:
        return []

    ratings_compare = ratings[name]
    final = []

    for diff_user, diff_ratings in ratings.items():
        if diff_user != name:
            similarity = sum([ratings_compare[i] * diff_ratings[i] for i in range(len(ratings_compare))])
            final.append((diff_user, similarity))

    final.sort(key=lambda x: (-x[1], x[0]))
    return final
 
def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''
    top_similar_users = similarities(name,ratings)[:numUsers]
    # if not top_similar_users:
    #     return [(item, 0.0) for item in items[:numUsers]]

    dic = {}

    for diff_user, similarity in top_similar_users:
        diff_ratings = ratings[diff_user]
        new_ratings = [similarity * x for x in diff_ratings]
        dic[diff_user] = new_ratings

    average_ratings = averages(items, dic)
    return average_ratings


    #final.sort(key=lambda x: (-x[1], x[0]))
        

if __name__ == '__main__':
    