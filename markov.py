#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:16:33 2018

SCRIPT:    markov-chains.py
AUTHOR(S): Courtney Taylor
PURPOSE:   Open educational materials for a seminar on digital culture
COPYRIGHT:  GNU General Public License v2. 
"""

# import libraries
import markovify 

"""
Combine text from Rilke and Aurelius
"""
# get raw text as string
with open("rilke.txt") as f:
    rilke = f.read()

with open("meditations.txt") as f:
    aurelius = f.read()

# build and combine the models
rilke_model = markovify.Text(rilke)
aurelius_model = markovify.Text(aurelius)
model_synthesis = markovify.combine([rilke_model, aurelius_model], 
    [ 1, 1 ])

# print five randomly-generated sentences
for i in range(2):
    print model_synthesis.make_short_sentence(140)
    