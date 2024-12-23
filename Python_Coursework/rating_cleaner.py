
def rating_cleaner(rating):
    """gets numeric portion from web rating

    Args:
        rating (str): text rating from web

    Returns:
        int: integer portion of rating
    """

    numeric_rating = int(rating[0])
    return numeric_rating


def rating_list_cleaner(rating_list):
    """cleans lists of ratings and returns numeric
        ratings lists

    Args:
        rating_list (list): list of text ratings

    Returns:
        list: list of integer ratings
    """
    numeric_list = []
    for rating in rating_list:
        numeric_rating = rating_cleaner(rating)
        numeric_list.append(numeric_rating)
    return numeric_list
