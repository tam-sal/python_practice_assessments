# -*- coding: utf-8 -*-

'''1 -Below, we’ve provided a list of lists. Use in statements to create variables with Boolean values - see the ActiveCode window for further directions.'''

L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
test1 = 'hola' in L
            
        

# Test if [5, 8, 7] is in the list L. Save to variable name test2
test2 = [5, 8, 7] in L


# Test if 6.6 is in the third element of list L. Save to variable name test3
test3 = 6.6 in L[2]


'''2 -Provided is a nested data structure. Follow the instructions in the comments below. Do not hard code.'''

nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
data = True if "data" in list(nested.keys()) else False
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = True if 24 in nested["data"] else False
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
whole = True if 'whole' not in nested["window"] else False 
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics = True if "physics" in nested else False

'''3 -The variable nested_d contains a nested dictionary with the gold medal counts for the top four countries in the past three Olympics. Assign the value of Great Britain’s gold medal count from the London Olympics to the variable london_gold. Use indexing. Do not hardcode.'''

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
london_gold = 0
for outer_key in nested_d:
    for inner_key in nested_d[outer_key]:
        if inner_key == 'Great Britain' and outer_key == "London":
            london_gold = (nested_d[outer_key][inner_key])


'''4 -Given the dictionary, nested_d, save the medal count for the USA from all three Olympics in the dictionary to the list US_count.'''

nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []
for v in nested_d.values():
    for k in v:
        if k == "USA":
            US_count.append(v[k])

'''5 -Iterate through the contents of l_of_l and assign the third element of sublist to a new list called third.'''

l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third = [item[2] for item in l_of_l]

'''6 -Given below is a list of lists of athletes. Create a list, t, that saves only the athlete’s name if it contains the letter “t”. If it does not contain the letter “t”, save the athlete name into list other.'''

athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t = []
other = []
for lis in athletes:
    for athlete in lis:
        if "t" in athlete:
            t.append(athlete)
        else:
            other.append(athlete)

'''7 -Write code to assign to the variable map_testing all the elements in lst_check while adding the string “Fruit: ” to the beginning of each element using mapping.'''

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing = list(map(lambda x: "Fruit: "+x  , lst_check))

'''8 -Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries that only contains the strings from countries that begin with B.'''

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']

b_countries = list(filter(lambda x: x[0] == "B" , countries))

'''9 -Below, we have provided a list of tuples that contain the names of Game of Thrones characters. Using list comprehension, create a list of strings called first_names that contains only the first names of everyone in the original list.'''

people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]

first_names = [y for x,y in people]


'''10 -Use list comprehension to create a list called lst2 that doubles each element in the list, lst.'''

lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [item *2 for item in lst]

'''11 -Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. Using list comprehension, create a new list passed that contains the names of students who passed the class (had a final grade of 70 or greater).'''

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]

passed = [x for x,y in students if y >= 70]

'''12 -Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the variable opposites if they are both longer than 3 characters each.'''

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']

l3 = list(zip(l1,l2))
opposites = list(filter(lambda x: (len(x[0]) > 3 and len(x[1]) > 3), l3))

'''13 -Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. From this list, create a new list called endangered that contains the names of species whose populations are below 2500.'''

species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]

pop_info = list(zip(species, population))

endangered = [x for x,y in pop_info if y < 2500]

################## Final Project ###################

'''This project will take you through the process of mashing up data from two different APIs to make movie recommendations. The TasteDive API lets you provide a movie (or bands, TV shows, etc.) as a query input, and returns a set of related items. The OMDB API lets you provide a movie title as a query input and get back data about the movie, including scores from various review sites (Rotten Tomatoes, IMDB, etc.).

You will put those two together. You will use TasteDive to get related movies for a whole list of titles. You’ll combine the resulting lists of related movies, and sort them according to their Rotten Tomatoes scores (which will require making API calls to the OMDB API.)

To avoid problems with rate limits and site accessibility, we have provided a cache file with results for all the queries you need to make to both OMDB and TasteDive. Just use requests_with_caching.get() rather than requests.get(). If you’re having trouble, you may not be formatting your queries properly, or you may not be asking for data that exists in our cache. We will try to provide as much information as we can to help guide you to form queries for which data exists in the cache.

Your first task will be to fetch data from TasteDive. The documentation for the API is at https://tastedive.com/read/api.

Define a function, called get_movies_from_tastedive. It should take one input parameter, a string that is the name of a movie or music artist. The function should return the 5 TasteDive results that are associated with that string; be sure to only get movies, not other kinds of media. It will be a python dictionary with just one key, ‘Similar’.

Try invoking your function with the input “Black Panther”.

HINT: Be sure to include only q, type, and limit as parameters in order to extract data from the cache. If any other parameters are included, then the function will not be able to recognize the data that you’re attempting to pull from the cache. Remember, you will not need an api key in order to complete the project, because all data will be found in the cache.'''

'''The cache includes data for the following queries:

q

type

limit

Black Panther
'''
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# main input is a string that is the name of a movie or music artist
# The function should return the 5 TasteDive results that are associated with that string; 
#be sure to only get movies, not other kinds of media. 
#It will be a python dictionary with just one key, ‘Similar’
import requests_with_caching
def get_movies_from_tastedive(name):
    base_url = "https://tastedive.com/api/similar"
    params_dic = {"q":name, "type":"movies", "limit":5}
    req = requests_with_caching.get(base_url, params = params_dic)
    return req.json()

v = get_movies_from_tastedive("Bridesmaids")


'''Please copy the completed function from above into this active code window. Next, you will need to write a function that extracts just the list of movie titles from a dictionary returned by get_movies_from_tastedive. Call it extract_movie_titles.'''

import requests_with_caching
def get_movies_from_tastedive(name):
    base_url = "https://tastedive.com/api/similar"
    params_dic = {"q":name, "type":"movies", "limit":5}
    req = requests_with_caching.get(base_url, params = params_dic)
    return req.json()

def extract_movie_titles(dic_movies):
    res_output = dic_movies['Similar']['Results']
    out_list = [d['Name'] for d in res_output]
    return out_list

'''Please copy the completed functions from the two code windows above into this active code window. Next, you’ll write a function, called get_related_titles. It takes a list of movie titles as input. It gets five related movies for each from TasteDive, extracts the titles for all of them, and combines them all into a single list. Don’t include the same movie twice.'''

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])

import requests_with_caching
def get_movies_from_tastedive(name):
    base_url = "https://tastedive.com/api/similar"
    params_dic = {"q":name, "type":"movies", "limit":5}
    req = requests_with_caching.get(base_url, params = params_dic)
    return req.json()

def extract_movie_titles(dic_movies):
    res_output = dic_movies['Similar']['Results']
    out_list = [d['Name'] for d in res_output]
    return out_list

def get_related_titles(movies_list):
    outer_list = [get_movies_from_tastedive(movie) for movie in movies_list]
    sub_lists = [extract_movie_titles(d) for d in outer_list]
    final_list = []
    for l in sub_lists:
        for movie in l:
            if movie not in final_list:
                final_list.append(movie)
    return final_list

'''Your next task will be to fetch data from OMDB. The documentation for the API is at https://www.omdbapi.com/

Define a function called get_movie_data. It takes in one parameter which is a string that should represent the title of a movie you want to search. The function should return a dictionary with information about that movie.

Again, use requests_with_caching.get(). For the queries on movies that are already in the cache, you won’t need an api key. You will need to provide the following keys: t and r. As with the TasteDive cache, be sure to only include those two parameters in order to extract existing data from the cache.'''

# some invocations that we use in the automated tests; 
#uncomment these if you are getting errors and want better error messages
# get_movie_data("Venom")
# get_movie_data("Baby Mama")
import requests_with_caching
def get_movie_data(movie_title):
    baseurl = 'http://www.omdbapi.com/'
    params_dic = {'t': movie_title, 'r': 'json'}
    req = requests_with_caching.get(baseurl, params = params_dic)
    return req.json()

movie_data = get_movie_data("Deadpool 2")
print(movie_data)

'''Please copy the completed function from above into this active code window. Now write a function called get_movie_rating. It takes an OMDB dictionary result for one movie and extracts the Rotten Tomatoes rating as an integer. For example, if given the OMDB dictionary for “Black Panther”, it would return 97. If there is no Rotten Tomatoes rating, return 0.'''

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))

import requests_with_caching
def get_movie_data(movie_title):
    baseurl = 'http://www.omdbapi.com/'
    params_dic = {'t': movie_title, 'r': 'json'}
    req = requests_with_caching.get(baseurl, params = params_dic)
    return req.json()

def get_movie_rating(omdb_dic):
    ratings = omdb_dic["Ratings"]
    for rating_dic in ratings:
        if 'Rotten Tomatoes' in rating_dic['Source']:
            rot_tom_value = int(rating_dic['Value'][:-1])
            return rot_tom_value
    return 0


'''Now, you’ll put it all together. Don’t forget to copy all of the functions that you have previously defined into this code window. Define a function get_sorted_recommendations. It takes a list of movie titles as an input. It returns a sorted list of related movie titles as output, up to five related movies for each input movie title. The movies should be sorted in descending order by their Rotten Tomatoes rating, as returned by the get_movie_rating function. Break ties in reverse alphabetic order, so that ‘Yahşi Batı’ comes before ‘Eyyvah Eyvah’.'''

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
import requests_with_caching
def get_movies_from_tastedive(name):
    base_url = "https://tastedive.com/api/similar"
    params_dic = {"q":name, "type":"movies", "limit":5}
    req = requests_with_caching.get(base_url, params = params_dic)
    return req.json()

def extract_movie_titles(dic_movies):
    res_output = dic_movies['Similar']['Results']
    out_list = [d['Name'] for d in res_output]
    return out_list

def get_related_titles(movies_list):
    outer_list = [get_movies_from_tastedive(movie) for movie in movies_list]
    sub_lists = [extract_movie_titles(d) for d in outer_list]
    final_list = []
    for l in sub_lists:
        for movie in l:
            if movie not in final_list:
                final_list.append(movie)
    return final_list

def get_movie_data(movie_title):
    baseurl = 'http://www.omdbapi.com/'
    params_dic = {'t': movie_title, 'r': 'json'}
    req = requests_with_caching.get(baseurl, params = params_dic)
    return req.json()

def get_movie_rating(omdb_dic):
    ratings = omdb_dic["Ratings"]
    for rating_dic in ratings:
        if 'Rotten Tomatoes' in rating_dic['Source']:
            rot_tom_value = int(rating_dic['Value'][:-1])
            return rot_tom_value
    return 0

def get_sorted_recommendations(movies_list):
    related_titles = get_related_titles(movies_list)
    movies_data = [get_movie_data(movie) for movie in related_titles]
    movies_rating = [get_movie_rating(movie) for movie in movies_data]
    mov_rat = dict(zip(related_titles, movies_rating))
    fin = sorted([k for k in mov_rat], key = lambda k: (mov_rat[k], k), reverse = True)
    return fin
    
h = get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
print(h)






