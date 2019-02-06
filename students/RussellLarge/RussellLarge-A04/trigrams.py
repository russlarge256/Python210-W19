#!/usr/bin/env python3

#-------------------------------------------------#
# Title: Trigrams
# Dev:   Rlarge
# Date:  1/31/2019
# ChangeLog: (Who, When, What)
#   RLarge, 01/31/2019, Created Script

#-------------------------------------------------#

# Import Modules
import sys
import random

# File location
file = r'C:\python210\2_2_19\sherlock.txt'



def ReadData(file):
    """Reads text from file source and appends to list"""
    with open("{}".format(file), 'r') as f:
        NewList = []
        for line in f:
            if line.__contains__("*** END OF"):
                break
            NewList.append(line)
        return " ".join(NewList)

def MakeWords(text):
    """Makes 'words' and filters out other characters"""
    if text.__contains__(",.!@#$%^&*"):
        text.replace('')
    words = text.split()
    NewData = []
    for word in words:
            NewData.append(word)
    return NewData

def BuildTrigrams(NewData):
    '''Creates pairs of words and appends them for each word set'''
    trigrams = {}
    for i in range(len(NewData)-2):
        pair = tuple(NewData[i:i + 2])
        follower = NewData[i + 2]
        trigrams.setdefault(pair, []).append(follower)

    return trigrams

def BuildText(trigrams):
    '''Builds text randomly and appends with trigrams'''
    newbuild = []
    newrange = range(15)
    for item in newrange:
        wordpair = list(random.choice(list(trigrams.keys())))
        for text in range(len(file)):
            pair = tuple(wordpair[-2:])
            wordpair.append(random.choice(trigrams[pair]))
        newbuild.extend(wordpair)
    newbuild = " ".join(newbuild)
    return newbuild

if __name__ == "__main__":
    '''Main run for script'''
    try:
        filename = file
    except IndexError:
        print("You must pass in a filename")
        sys.exit(1)

    in_data = ReadData(file)
    words = MakeWords(in_data)
    word_pairs = BuildTrigrams(words)
    new_text = BuildText(word_pairs)

    print(new_text)
