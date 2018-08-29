#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
AUTHOR: Courtney Taylor
DESCRIPTION: python text generator
LICENSE: GNU General Public License v2
"""

import random

random.seed()

# lists of nouns
nouns = ["sailor", 
         "jester", 
         "apple", 
         "space"]

# lists of verbs
verbs = ["jests", 
         "sails", 
         "eats", 
         "rockets"]

# lists of adjectives
adjectives = ["raucous", 
              "jaunty", 
              "quiet", 
              "irritable",
              "green"]

# lists of adverbs
adverbs = ["slowly", 
           "sheepishly", 
           "vigorously",
           "churlishly"]

# select random words from lists
noun = random.choice(nouns)

verb = random.choice(verbs)

adjective = random.choice(adjectives)

adjective_b = random.choice(adjectives)

adverb = random.choice(adverbs)

#word poem
print "The " + adjective + " " + noun + " "

# for loop to iterate through verbs
i = 1
for verb in verbs:
    whitespace = " " * i
    print whitespace + verb
    i = i + 1
    


## concatenation
#print "The " + adjective + " " + noun + " " + verb + " " + adverb
#
##string formatting
#print "The {adj}, {adj_b} {n} {v}." .format(adj=adjective, 
#           adj_b=adjective_b, n=noun, v=verb)



#i = 0
#for noun in nouns:
#    print nouns [i]
#    i = i + 1
#    
#j = 0
#for verb in verbs: 
#    print verbs [j]
#    j = j + 1
#    
#k = 0 
#for adjective in adjectives: 
#    print adjectives [k]
#    k = k + 1
    