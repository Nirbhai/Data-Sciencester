# -*- coding: utf-8 -*-
"""

Let's start with a joke:
    Data scientist is someone who knows more 
    statistics than a computer scientist
    and more computer science than a statistician.
        


Author	: Nirbhai Singh
E-Mail	: chittamor@gmail.com


"""

from collections import Counter, defaultdict

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
    ]

friendship_pairs = [
    (0, 1), (0, 2), (1, 2),
    (1, 3), (2, 3), (3, 4),
    (4, 5), (5, 6), (5, 7),
    (6, 8), (7, 8), (8, 9)
    ]

# intialize the dict with an empty list for each user id
friendships = {user ["id"]: [] for user in users}

# And loop over the friendship pairs to populate it
for i,j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

def number_of_friends(user):
    """
    How many friends does __user__ have?

    Parameters
    ----------
    user : dict
        Dictionary containing two key value pairs.
        1st key: "id" - value: number
        2nd key: "name" - value: string

    Returns
    -------
    Number
    total number of friends of the __user__.

    """
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user) for user in users)

assert total_connections == 24

# Total number of users is length of the users list
num_users = len(users)

avg_connections = total_connections / num_users

assert avg_connections == 2.4

# create a list (user id, number of friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
num_friends_by_id_me = [ (_, len(friendships[_])) for _ in friendships]

assert num_friends_by_id == num_friends_by_id_me

assert Counter(num_friends_by_id) == Counter(num_friends_by_id_me)

def foaf_ids_bad(user):
    """
    This is a bad function for finding friends of friends of __user__

    Parameters
    ----------
    user : dict
        Dictionary containing two key value pairs.
        1st key: "id" - value: number
        2nd key: "name" - value: string

    Returns
    -------
    A list of ids (friends of friends of __user__)

    """
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]

print (foaf_ids_bad(users[0]))

def friends_of_friends(user):
    """
    This is a good function for finding friends of friends of __user__

    Parameters
    ----------
    user : dict
        Dictionary containing two key value pairs.
        1st key: "id" - value: number
        2nd key: "name" - value: string

    Returns
    -------
    A dictionary containing count of mutual friends of __user__ with each friend which are not direct friends

    """
    return Counter(foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]
            if foaf_id != user["id"]
            and foaf_id not in friendships[user["id"]])

print(friends_of_friends(users[3]))

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

def data_scientists_who_like(target_interest):
    """
    Find the ids of all users who like the target interest

    Parameters
    ----------
    target_interest : string
        interest of a data scientist

    Returns
    -------
    list of user ids which like the target interest

    """
    return [user_id 
            for user_id, target_interest in interests
        ]

# keys are interests and values are list of user ids with that interest
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# keys are user ids and values are list of interests for that user id
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)


