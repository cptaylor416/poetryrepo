#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SCRIPT:    markov-chains.py
AUTHOR(S): Courtney Taylor
PURPOSE:   Open educational materials for a seminar on digital culture
COPYRIGHT:  GNU General Public License v2. 
"""

print "Nowhere you can go is more peaceful."


# import libraries
import markovify 

"""
Combine text from Aurelius's Meditations and Rilke's Collected Poems
"""
# get raw text as string
with open("../cptaylor-poetry-repository/meditations.txt") as f:
    aurelius = f.read()

with open("../cptaylor-poetry-repository/rilke.txt") as f:
    rainer = f.read()

# build and combine the models
aurelius_model = markovify.Text(aurelius)
rainer_model = markovify.Text(rainer)
model_synthesis = markovify.combine([aurelius_model, rainer_model], 
    [ 20, 2 ])

# print five randomly-generated sentences
for i in range(1):
    print model_synthesis.make_sentence()
    
import random

random.seed()


# lists of verbs
verbs = ["pours", 
         "reaches", 
         "climbs", 
         "sinks"]


# select random words from lists
verb = random.choice(verbs)


print "It"

# for loop to iterate through verbs
i = 1
for verb in verbs:
    whitespace = " " * i
    print whitespace + verb
    i = i + 1


# additional phrase
print "     as if standing on fishes."

