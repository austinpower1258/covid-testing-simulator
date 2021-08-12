# YSPA 2019 - PSET#4 Problem 2: 
# This fall, about 3000 Yale undergraduates will be on campus, taking mostly remote classes from 
# their dorm rooms, lounges, the libraries, etc. (and some classes can be outside while the 
# weather is good). There will be rules for social distancing and mask wearing, and students will 
# get virus detection tests every week, and those that test positive will undergo contact tracing 
# interviews and be isolated somewhere else in supported isolation. 
# Virus testing is slow in the US because the testing reagent takes time and money to make, and 
# we need to do millions of tests per month. One idea that could stretch the reserves of the 
# reagent supply is "pool testing". Suppose you have 10 samples to test. You could test each one 
# of them separately, using a unit of reagent for each of the 10 tests. OR… you could pool the 
# samples, test that pool, and use one unit of reagent for that pooled test. If it's negative, then all 
# 10 of those students are cleared (with all of the caveats about false negatives from the last 
# problem), and you've saved 9 units of reagent. However, if the virus detection test is positive, 
# then one (or more) of those samples was positive for the virus, and you'll need to go back and 
# retest a smaller pool. 
# Can you think of a pool testing strategy or an algorithm for 3000 samples per week that will 
# optimize reagent use efficiency? Assume that you can get as many samples as you need from 
# each student (so if a pooled sample tests positive, it is no effort to get more samples from those 
# individual people for further testing).
# Can you think of any situation where pooled testing would actually use more reagent than 
# testing each sample individually? 

# [My Solution]: I designed a recursive function that would do as expected from the algorithm above. 
# The groups would branch out to more groups of 2 as the pooled tests remain positive, and every 
# time the function is called, the reagent count would need to be increased by 1. We only need to 
# check whether the length of groups gets to 1 - in that case, we would be done. We can use for loops, 
# checking the length if the group is more than length 1 and there is a positive pooled test, and 
# this can determine which groups that we need to add together (form a new group of ½ the size). 
# We can then pass these new groups into the recursive function, where it will keep on going until 
# the pool tests are negative or when the array length is 1. Assumptions: ratio of infected is 1%.

import random
import math

#generate an array of n population of people
# 1 denotes infected, 0 denotes healthy
#ratio defines the COVID-infected rate
def generate_sample_cases(ratio, population):
    list = []
    infected_number = int(ratio * population)
    healthy_number = int((1 - ratio) * population)
    #in order to insert a ratio of infected people
    for i in range (0, infected_number):
        list.append(1)
    #in order to insert a ratio of healthy people
    for j in range (0, healthy_number):
        list.append(0)

    #shuffles the list to random order
    random.shuffle(list)
    return list

#generate the array
cases = generate_sample_cases(0.01, 3000)
print(cases)

#declare a variable reagants (number of reagants)
reagants = 0

def pool_testing(people):
    positive = False
    #in recursive functions, we need to store a global variable
    #we cannot initialize it inside the function
    global reagants

    #increment reagants everytime the function is run
    #since this is recursive
    reagants += 1

    #since we are branching by 2, we need to initialize 2 arrays
    group1 = []
    group2 = []

    #check to see if there are infected people in the groups
    if (len(people) != 1):
        for x in range(len(people)):
            if (people[x] == 1):
                positive = True

    #if there are infected people and the array length is greater than 1
    if (positive and len(people) >= 1):
        for i in range(0, int(len(people)/2)):
            group1.append(people[i])
        #branch out the recursion
        pool_testing(group1)

        #likewise for the second branch of groups
        for j in range(int(len(people)/2), int(len(people))):
            group2.append(people[j])

        pool_testing(group2)
    #return reagants at the end - should give us our answer
    return reagants

print(pool_testing(cases))
