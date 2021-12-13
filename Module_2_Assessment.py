# -*- coding: utf-8 -*-


'''1 -The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.'''

file_name = "travel_plans.txt"
ref_file = open(file_name, "r")
contents = ref_file.read()
num = len(contents)
print(num)
ref_file.close()


'''2 -We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.'''

my_file = "emotion_words.txt"
ref_file = open(my_file, "r")
line_lists = ref_file.readlines()
num_words = 0
for line in line_lists:
    line = line.strip().split()
    words_in_line = len(line)
    num_words += words_in_line
print(num_words)

'''3 -Assign to the variable num_lines the number of lines in the file school_prompt.txt.'''

file_ref = open("school_prompt.txt", "r")
num_lines = 0
for line in file_ref:
    num_lines += 1
print(num_lines)

'''4 -Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.'''

file_ref = open("school_prompt.txt", "r")
beginning_chars = file_ref.read()[:30]
print(str(beginning_chars))

'''5 -Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.'''

file_ref = open("school_prompt.txt", "r")
lines_in_file = file_ref.readlines()
three = []
for line in lines_in_file:
    words_in_line = line.strip().split()
    third_word = words_in_line[2]
    three.append(third_word)
print(three)

'''6 - Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.'''

file_ref = "emotion_words.txt"
emotions_file = open(file_ref, "r")
lines_in_emotions = emotions_file.readlines()
emotions = []
for line in lines_in_emotions:
    line_sub_list = line.strip().split()
    first_word = line_sub_list[0]
    emotions.append(first_word)
print(emotions)

'''7 -Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.'''

my_file = "travel_plans.txt"
travel_file = open(my_file, "r")
first_chars = travel_file.read()[:33]
print(first_chars)

'''8 -Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.'''

p_words = []
my_file = "school_prompt.txt"
school_file = open(my_file, "r")
lines_list = school_file.readlines()
for line in lines_list:
    line = line.strip().split()
    for word in line:
        if "p" in word:
            p_words.append(word)
print(p_words)

'''9 -Provided is a dictionary called US_medals which has the first 70 metals that the United States has won in 2016, and in which category they have won it in. Using dictionary mechanics, assign the value of the key "Fencing" to a variable fencing_value. Remember, do not hard code this.'''

US_medals = {"Swimming": 33, "Gymnastics": 6, 
             "Track & Field": 6, "Tennis": 3, 
             "Judo": 2, "Rowing": 2, "Shooting": 3, 
             "Cycling - Road": 1, "Fencing": 4, "Diving": 2, 
             "Archery": 2, "Cycling - Track": 1, "Equestrian": 2, 
             "Golf": 1, "Weightlifting": 1}

fencing_value = US_medals["Fencing"]
print(fencing_value)


'''10 -The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the number of credits. Find the total number of credits taken this semester and assign it to the variable credits. Do not hardcode this – use dictionary accumulation!'''

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for credit in Junior.values():
    credits += credit
print(credits)

'''11 -Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.'''

str1 = "peter piper picked a peck of pickled peppers"
freq = {}
for c in str1:
    if c not in freq:
        freq[c] = 0
    freq[c] += 1
print(freq)

'''12 -Create a dictionary, freq_words, that contains each word in string str1 as the key and its frequency as the value.'''

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"
freq_words = {}
words = str1.split()
for word in words:
    if word not in freq_words:
        freq_words[word] = 0
    freq_words[word] += 1
print(freq_words)

'''13 -Create the dictionary characters that shows each character from the string sally and its frequency. Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.'''

sally = "sally sells sea shells by the sea shore"
characters = {}
for char in sally:
    if char not in characters:
        characters[char] = 0
    characters[char] += 1
best_char = list(characters.keys())[0]
for key in characters:
    if characters[key] > characters[best_char]:
        best_char = key
print(key)

'''14 -Find the least frequent letter. Create the dictionary characters that shows each character from string sally and its frequency. Then, find the least frequent letter in the string and assign the letter to the variable worst_char.'''

sally = "sally sells sea shells by the sea shore and by the road"
characters = {}
for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] += 1

worst_char = list(characters.keys())[0]
for key in characters:
    if characters[key] < characters[worst_char]:
        worst_char = key
print(key)
print(characters[key])

'''15 -Create a dictionary named letter_counts that contains each letter and the number of times it occurs in string1. Challenge: Letters should not be counted separately as upper-case and lower-case. Intead, all of them should be counted as lower-case.'''

string1 = "There is a tide in the affairs of men, Which taken at the flood, leads on to fortune. Omitted, all the voyage of their life is bound in shallows and in miseries. On such a full sea are we now afloat. And we must take the current when it serves, or lose our ventures."
low_str = string1.lower()
letter_counts = {}
for c in low_str:
    if c not in letter_counts:
        letter_counts[c] = 0
    letter_counts[c] += 1
print(letter_counts)

'''16 -Create a dictionary called low_d that keeps track of all the characters in the string p and notes how many times each character was seen. Make sure that there are no repeats of characters as keys, such that “T” and “t” are both seen as a “t” for example.'''

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
p_low = p.lower()
low_d = {}
for c in p_low:
    if c not in low_d:
        low_d[c] = 0
    low_d[c] += 1
print(low_d)

'''17 -Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”.'''

def length(lst):
    long = "Longer than 5"
    short = "Less than 5"
    n = len(lst)
    if n >= 5:
        return long
    return short

'''18 -You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals.'''

def divide(m):
    u = m / 2
    return u
def sum(h):
    y = divide(h)
    y += 6
    return y

'''19 -The list below, tuples_lst, is a list of tuples. Create a list of the second elements of each tuple and assign this list to the variable country.'''

tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]

country = [item[1] for item in tuples_lst]

'''20 -With only one line of code, assign the variables city, country, and year to the values of the tuple olymp.'''

olymp = ('Rio', 'Brazil', 2016)
city, country, year = olymp

'''21 -Given is the dictionary, gold, which shows the country and the number of gold medals they have earned so far in the 2016 Olympics. Create a list, num_medals, that contains only the number of medals for each country. You must use the .items() method. Note: The .items() method provides a list of tuples. Do not use .keys() method.'''

gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals = [item[1] for item in gold.items()]


'''22 -Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).'''

def sublist(my_list):
    final_list = []
    my_list_len = len(my_list)
    idx = 0
    while idx < my_list_len and my_list[idx] != 5:
        final_list.append(my_list[idx])
        idx += 1
    return final_list


'''23 -Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.'''

def check_nums(my_list):
    final_list = []
    my_list_len = len(my_list)
    idx = 0
    while idx < my_list_len and my_list[idx] != 7:
        final_list.append(my_list[idx])
        idx += 1
    return final_list

'''24 -Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).'''

def sublist(my_list):
    final_list = []
    my_list_len = len(my_list)
    idx = 0
    while idx < my_list_len and my_list[idx] != "STOP":
        final_list.append(my_list[idx])
        idx += 1
    return final_list

'''25 -Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing'''

def beginning(str_list):
    final_list = []
    idx = 0
    while idx < len(str_list) and str_list[idx] != "bye" and idx < 10:
        final_list.append(str_list[idx])
        idx += 1
    return final_list

'''26 -Write a function, test, that takes in three parameters: a required integer, an optional boolean whose default value is True, and an optional dictionary, called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True, the function should test to see if the integer is a key in the dictionary. The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.'''

def test(x, check = True, dict1 = {2:3, 4:5, 6:8}):
    if check == True:
        if x in list(dict1.keys()):
            return dict1[x]
        else:
            return False
    else:
        return check

'''27 -Write a function called checkingIfIn that takes three parameters. The first is a required parameter, which should be a string. The second is an optional parameter called direction with a default value of True. The third is an optional parameter called d that has a default value of {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}. Write the function checkingIfIn so that when the second parameter is True, it checks to see if the first parameter is a key in the third parameter; if it is, return True, otherwise return False.

But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third. If it’s not, the function should return True in this case, and if it is, it should return False.'''

def checkingIfIn(str1, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if str1 in list(d.keys()):
            return True
        else:
            return False
    else:
        if str1 not in list(d.keys()):
            return True
        return False

'''28 -We have provided the function checkingIfIn such that if the first input parameter is in the third, dictionary, input parameter, then the function returns that value, and otherwise, it returns False. Follow the instructions in the active code window for specific variable assignmemts.'''

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false

# Call the fucntion so that it returns True and assign it to the variable c_true

# Call the function so that the value of fruit is assigned to the variable fruit_ans

# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check

c_false = checkingIfIn("house", True)
c_true = checkingIfIn("house", False)

fruit_ans = 19
checkingIfIn("h", direction = True, d = {'apple': 2, 'pear': 1, 'fruit': fruit_ans, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7})
param_check = 8
checkingIfIn(param_check, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7})

'''29 -Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.'''

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
top_three = sorted(medals, key = lambda k: medals[k], reverse = True)[:3]

'''30 -We have provided the dictionary groceries. You should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.'''

groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = sorted(groceries, key = lambda k: groceries[k], reverse = True)

'''31 -Create a function called last_four that takes in a single ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use the resulting function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.'''

def last_four(x):
    x = str(x)
    x = x[-4:]
    return x


ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_ids = sorted(ids, key = last_four)

'''32 -Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.'''

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id = sorted(ids, key = lambda x: str(x)[-4:])

'''33 -Sort the following list by each element’s second letter a to z. Do so by using lambda. Assign the resulting value to the variable lambda_sort.'''

ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_arg = lambda x: x[1]
lambda_sort = sorted(ex_lst, key = lambda_arg)

##################### Final ################
'''We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.

Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)'''

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return word

'''Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.'''

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return word

for p_word in positive_words:
    positive_words[positive_words.index(p_word)] = p_word.lower()
def get_pos(a_str):
    pos_count = 0
    s_str = a_str.strip().split()
    s_str = [strip_punctuation(word).lower() for word in s_str]
    for item in s_str:
        if item in positive_words:
            pos_count += 1
    return pos_count

'''Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.'''

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())         


def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return word
for neg_word in negative_words:
    negative_words[negative_words.index(neg_word)] = neg_word.lower()

def get_neg(a_str):
    neg_count = 0
    s_str = a_str.strip().split()
    s_str = [strip_punctuation(word).lower() for word in s_str]
    for item in s_str:
        if item in negative_words:
            neg_count += 1
    return neg_count

'''Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.'''

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

for p_word in positive_words:
    positive_words[positive_words.index(p_word)] = p_word.lower()
for neg_word in negative_words:
    negative_words[negative_words.index(neg_word)] = neg_word.lower()

def strip_punctuation(word):
    for char in word:
        if char in punctuation_chars:
            word = word.replace(char, "")
    return word

def get_pos(a_str):
    pos_count = 0
    s_str = a_str.strip().split()
    s_str = [strip_punctuation(word).lower() for word in s_str]
    for item in s_str:
        if item in positive_words:
            pos_count += 1
    return pos_count

def get_neg(a_str):
    neg_count = 0
    s_str = a_str.strip().split()
    s_str = [strip_punctuation(word).lower() for word in s_str]
    for item in s_str:
        if item in negative_words:
            neg_count += 1
    return neg_count

with open("project_twitter_data.csv", "r") as td:
    file_lines = td.readlines()[1:]
    file_lines = [item.strip().split(",") for item in file_lines]
    d = {}
    rt_count = []
    rp_count = []
    pos_score = []
    neg_score = []
    nt_score_exp = []
    for tweet_text, retweet_count, reply_count in file_lines:
        rt_count += [retweet_count]
        d["Number of Retweets"] = rt_count
        rp_count += [reply_count]
        d["Number of Replies"] = rp_count
        tt = strip_punctuation(tweet_text).lower()
        pos_score += [get_pos(tt)]
        d["Positive Score"] = pos_score
        neg_score += [get_neg(tt)]
        d["Negative Score"] = neg_score
        net_score = get_pos(tt) - get_neg(tt)
        nt_score_exp += [net_score]
        d["Net Score"] = nt_score_exp
        
        values_nbr_rt = d["Number of Retweets"]
        values_nbr_rp = d["Number of Replies"]
        values_pos_score = d["Positive Score"]
        values_neg_score = d["Negative Score"]
        values_net_score = d["Net Score"]
    with open("resulting_data.csv", "w") as rd:
        header = "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score" 
        rd.write(header+"\n")
        
        for i in range(len(file_lines)):
            row = str(values_nbr_rt[i])+","+str(values_nbr_rp[i])+","+str(values_pos_score[i])+","+str(values_neg_score[i])+","+str(values_net_score[i])
            rd.write(row+"\n")

