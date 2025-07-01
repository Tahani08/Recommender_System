'''
@author: Tahani Hassan
'''
from RecommenderEngine import recommendations


def makerecs(name, items, ratings, numUsers, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists. 
    The first list is the top items rated by the rater called name (string).
    The second list is the top items not seen/rated by name (string)
    '''
    recommended_items = recommendations(name, items, ratings, numUsers)

    rated = []
    unrated = []
    user_ratings = ratings[name]

    for item, score in recommended_items:
        index = items.index(item)
        if user_ratings[index] != 0:
            rated.append((item, score))
        else:
            unrated.append((item, score))

    rated = rated[:top]
    unrated = unrated[:top]

    return (rated, unrated)

    pass


if __name__ == '__main__':
    pass
             



