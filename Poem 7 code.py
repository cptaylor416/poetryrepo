#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SCRIPT:    markov-chains.py
AUTHOR(S): Courtney Taylor
PURPOSE:   Open educational materials for a seminar on digital culture
COPYRIGHT:  GNU General Public License v2. 
"""


poem =  "Nowhere you can go is more peaceful.\n"

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
    [ 2, 20 ])

# print five randomly-generated sentences
for i in range(1):
    poem = poem + model_synthesis.make_sentence() + "\n"
    
import random

random.seed()


# lists of verbs
verbs = ["pours", 
         "reaches", 
         "climbs", 
         "sinks"]


# select random words from lists
verb = random.choice(verbs)


poem = poem + "It" + "\n"

# for loop to iterate through verbs
i = 1
for verb in verbs:
    whitespace = " " * i
    poem = poem + whitespace + verb + "\n"
    i = i + 1

# additional phrase
poem = poem +  "     as if standing on fishes."
print poem

# get raw text as string with the write (w) or append (a) option
with open("poem_7.txt", "w") as p:


    p.write(poem)


# get raw text as string with the write (w) or append (a) option
with open("poem_7.md", "w") as p:

    # write a header in markdown
    p.write("## Poem 7\n")
    p.write("```\n")
    p.write(poem)
    p.write("\n```")


