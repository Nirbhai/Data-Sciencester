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

### Finding key connectors ###

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

### Data Scientists you may know ###

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

def most_common_interests_with (user):
    """
    To find out who has the most number of common interests with __user__

    Parameters
    ----------
    user : dict
        Dictionary containing two key value pairs.
        1st key: "id" - value: number
        2nd key: "name" - value: string

    Returns
    -------
    

    """
    return Counter(
        interested_user_id
        for interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
        )

### Salaries and experience ###

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# Keys are years, values are lists of the salaries for each tenure.
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

# Keys are years, each value is average salary for that tenure.
average_salary_by_tenure = {
    tenure: sum(salaray)/len(salaray)
    for tenure, salaray in salary_by_tenure.items()
    }

assert average_salary_by_tenure == {
    0.7: 48000.0,
    1.9: 48000.0,
    2.5: 60000.0,
    4.2: 63000.0,
    6: 76000.0,
    6.5: 69000.0,
    7.5: 76000.0,
    8.1: 88000.0,
    8.7: 83000.0,
    10: 83000.0
}

def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


# Keys are tenure buckets, values are lists of salaries for that bucket.
salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# Keys are tenure buckets, values are average salary for that bucket
average_salary_by_bucket = {
  tenure_bucket: sum(salaries) / len(salaries)
  for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

assert average_salary_by_bucket == {
    'between two and five': 61500.0,
    'less than two': 48000.0,
    'more than five': 79166.66666666667
}

#print (average_salary_by_bucket)

### Paid accounts ###

"""
Years of exp : Paid accounts
0.7 paid
1.9 unpaid
2.5 paid
4.2 unpaid
6.0 unpaid
6.5 unpaid
7.5 unpaid
8.1 unpaid
8.7 paid
10.0 paid
"""

def predict_paid_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"

### Topics of interest ###

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), 
    (0, "Java"), (0, "Spark"), (0, "Storm"),
    (0, "Cassandra"), (1, "NoSQL"), (1, "MongoDB"),
    (1, "Cassandra"), (1, "HBase"), (1, "Postgres"),
    (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), 
    (3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), 
    (3, "probability"), (4, "machine learning"), (4, "regression"), 
    (4, "decision trees"), (4, "libsvm"), (5, "Python"),
    (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"), 
    (5, "programming languages"), (6, "statistics"), (6, "probability"),
    (6, "mathematics"), (6, "theory"), (7, "machine learning"), 
    (7, "scikit-learn"), (7, "Mahout"), (7, "neural networks"),
    (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

words_and_counts = Counter(word
                           for user, interest in interests
                           for word in interest.lower().split())

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
        