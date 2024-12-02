# AOC 2024 Day 1: Historian Hysteria
# Part 1:
import pandas as pd
from collections import Counter
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

# need to compare each element of left list individually against right list...
multipleList = []
for i in range(len(leftSorted)):
    for j in range(len(rightSorted)):
        if(leftSorted[i] == rightSorted[j]):
            multipleInstance = rightSorted[j]
            multipleList.append(multipleInstance)
sortedMultipleList = sorted(multipleList)

answer = 0
answerList = []

# Creates a list of the common elements. 

someList = list(set(leftSorted).intersection(rightSorted))
sortedSomeList = sorted(someList)
for i in range(len(sortedSomeList)):
    for j in range(len(sortedMultipleList)):
        if (sortedSomeList[i] == sortedMultipleList[j]):
            countedList = sortedMultipleList.count(sortedSomeList[i])
            answer = countedList * sortedSomeList[i]
    answerList.append(answer)
print("\nSimilarity score: ",sum(answerList))
# Correct Answer: 18650129