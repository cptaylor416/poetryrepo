#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:10:43 2018

@author: courtneytaylor
"""

import random

names = ["Tiger", "Tony"]
pronouns = ["he", "she", "it"]

# indexing list
print pronouns[1]

name = random.choice(names)
pronoun = random.choice(pronouns)

print pronoun.capitalize() + " " + name


print "Once upon a time {n} threw {pronoun} overboard.".format(n=name, 
        pronoun=pronoun.capitalize())

roll = random.randint (1,6)
print "{name} rolled a {roll}".format(name=name,roll=roll)

#if roll == 1:
 #   print "Success! " + pronoun + " rolled a " + str(roll)
 #   print "Success! {pronoun} rolled a {roll}".format(pronoun=pronoun,
 #   roll=roll)
    
if roll == 1:
    print "Bad luck!"
elif roll == 6:
    print "Good luck!"
else: 
    print "not so bad luck!"


     

#white space
#whitespace = " " * 10
#print whitespace + "hello world"


#whitespace with random interger
#i = random.randint (1,10)
#whitepsace = " " * i
#print whitespace + "hello world"
