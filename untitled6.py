#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 19:29:00 2018

@author: courtneytaylor
"""
mylist = []
for i in range(0,10):
    mylist.append ("hello world " + str(i))
    print mylist[i]



#with open ("poem.md", "w") as p: 
#    for i in range(1,10):
#        poem = "hello world " + str(i)
#        print poem
#        p.write(poem)
#        p.write("\n")