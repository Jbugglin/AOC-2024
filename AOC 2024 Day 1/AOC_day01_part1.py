# AOC 2024 Day 1: Historian Hysteria
# Part 1:
import pandas as pd
import csv
import operator
df = pd.read_csv('AOC 2024 Day 1\AOC_day01_puzzleInput.csv')

# original csv to list.
locations = df['locationID'].str.split().tolist()

# code to split into 2 separate lists
leftList, rightList = map(list, zip(*locations))

# Convert the string lists to int!
convertedLeftList = list(map(int, leftList))
convertedRightList = list(map(int, rightList))

# sort smallest - largest each list
leftSorted = sorted(convertedLeftList)
rightSorted = sorted(convertedRightList)

# find the difference between the sorted lists
answerList = []
for i in range(len(leftSorted)):
    if (leftSorted[i] > rightSorted[i]):
        distance = leftSorted[i] - rightSorted[i]
        answerList.append(distance)
    elif (leftSorted[i] < rightSorted[i]):
        distance = rightSorted[i] - leftSorted[i]
        answerList.append(distance)

print("\nThe total distance: ", sum(answerList))
# Correct Answer: 2904518