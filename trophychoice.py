
## Overview:
## This is a simple and totally over-engineered script to help choose which machine within the TJ Null / NetSecFocus Trophy Room OSCP prep
## list to do next.
## Instead of overanalyzing the next move, let python make the choice instead.
## I included weighting, with a 90/10 selection bias towards the normal suggested boxes rather than the 'harder boxes to try out'
#--------------------------------------------------------------
## Usage:
## [1] - pg practice
## [2] - pg play
## [3] - HTB (updated 2022 only)
## Simple run python trophychoice.py
## If you would like to change the weighting to further increase (or decrease) the likelihood of receiving the 'harder'/potentially beyond-oscp
## level boxes, simply change the numbers in weights
import random
import sys

def get_file():

    if sys.argv[1] == '1':
        file_name = 'pg_practice.txt'
        total = 50
        hard = 10
        return file_name, total, hard
    if sys.argv[1] == '2':
        file_name = 'pg_play.txt'
        total = 21
        hard = 8
        return file_name, total, hard
    if sys.argv[1] == '3':
        file_name = 'htb_2022.txt'
        total = 10
        hard = 0
        return file_name, total, hard
    else:
        file_name = 'pg_practice.txt'
        total = 50
        hard = 10
        return file_name, total, hard


def choose(file_name, total, hard):
    if not file_name:
        file_name = 'pg_practice.txt'

    with open(file_name, 'r') as m:
        line = m.readlines()
        linenum = len(line)
    #print(total, hard)
    major = (total - hard)

    # Set the weights for each line index
    # PG Practice -------------------------

    #weights
    if hard > 0:
        # 90 / 10
        weights = ([0.90] * major) + ([0.1] * hard)
        # 80 / 20
        # weights = ([0.80] * major) + ([0.2] * hard)
        # 70 / 30
        # weights = ([0.80] * major) + ([0.2] * hard)
        # no weighting
        #weight = 0
    else:
        weights = 0


    # Use the random.choices function to select a line index based on the weights


    if weights != 0:
        rand_num = random.choices(range(0, linenum), weights=weights, k=1)[0]
        # Print the randomly selected line
        print(f'Next machine: {line[rand_num]}')
        # for debugging
        print(weights[rand_num])
    elif weights == 0:
        rand_num = random.randrange(0,linenum)
        print(f'Next machine: {line[rand_num]}')

def main():
    print('Pick a random machine from TJNulls OSCP prep sheet!')
    print('''
    Usage:
        ## [1] - pg practice
        ## [2] - pg play
        ## [3] - HTB (updated 2022 only)
        ## Simply run python trophychoice.py num
        ## python trophychoice.py 1 
    ''')
    file_name, total, hard = get_file()
    choose(file_name, total, hard)

main()