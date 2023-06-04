from enum import Enum
import csv

dic = {
    'X' : 0,
    'Y' : 1,
    'Z' : 2,
    'A' : 0,
    'B' : 1,
    'C' : 2
}
    
"""the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won)."""


with open("input.txt", "r") as file:
    score = 0
    csv_reader = csv.reader(file, delimiter=' ')
    for row in csv_reader:
        enemy, you = row
        enemy = dic[enemy]
        you = dic[you]

        score += you + 1
        score += int(you%3 == (enemy+1)%3) * 6 
        score += int(you == enemy) * 3

print(score)
        

file.close()