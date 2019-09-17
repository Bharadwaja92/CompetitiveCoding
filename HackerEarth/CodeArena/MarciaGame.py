""""""
"""
Valentina is looking for a new game to play with her friends. She asks her mom Marcia for an idea. After a moment Marcia described to girls the following simple game.
Girls are divided into n teams, indexed 1 through n. Each girl chooses a lowercase letter, one of 'a' - 'z'. Of course, some girls can choose the same letter. Then, Marcia, as a judge, shows a string s, consisting of lowercase letters. For each letter in s, each girl with the same letter gets one point.
We define the score of a team as the total number of points of its members.
Your task is to find the winning team, determined according to the following rules:

The winning team is the one with the largest score.
In case of a tie between two or more teams, the one with the fewest members wins.
If there is still a tie between two or more teams then the one with the lowest index wins.
Given all the information about the game, find the index of the winning team.

Input format
The first line of the input contains one integer T denoting the number of test cases.
The first line of each test case description contains an integer n and a string s denoting the number of teams and a 
string showed by Marcia.
The i-th of the next n lines contains one non-empty string containing letters chosen by girls in the i-th team. The 
length of a string is equal to the number of members in a team.

All strings in the input consist of lowercase letters only.

Output format:  For each test case, output a single line containing the 1-based index of the winning team.

SAMPLE INPUT 
3
2 qwopwasp
wdw
abco
5 eeeessaa
valentina
esta
jugando
con
marcia
5 ahi
valentina
esta
jugando
con
susamigas
SAMPLE OUTPUT 
1
2
1
Explanation
In the first sample test case, there are  teams. The string showed by Marcia is . There are two letters 'w' in s, so 
two points are given to every girl who has chosen a letter 'w'.
Team 1 has three members. Two of them has chosen a letter 'w', and the other one has chosen a letter 'd'. The two girls 
get two points each, but the other girl has zero points because a letter 'd' doesn't occur in s at all. 
The score of team 1 is 2 + 2 = 4.

Team 2 has four members. A girl who has chosen a letter 'a' gets one point, and so does a girl who has chosen a letter 
'o'. The score of team 2 is 1 + 1 = 2.
So, in the first sample test case there is no tie and team 1 clearly wins.
"""
from collections import Counter

t = int(input())

while t > 0:
    l1 = input().split(' ')
    n, s = int(l1[0]), l1[1]
    points = dict(Counter(s))    # # Get num points for s
    numTeamMembers, scores = [], []
    for i in range(n):
        g = input()    # Each team's  string
        numTeamMembers.append(len(g))
        score = 0
        for c in g:
            if c in points:
                score += points[c]
        scores.append(score)

    print('scores are', scores)
    maxScore = max(scores)

    teamsWithMaxScore = [m for m in range(len(scores)) if scores[m] == maxScore]  # 0-indexed
    print('teamsWithMaxScore are', teamsWithMaxScore)

    if len(teamsWithMaxScore) == 1:
        print(teamsWithMaxScore[0] + 1, 'is the winner')
    else:
        print('Else case')
        teamsWithMaxScoreTeamSize = [numTeamMembers[m] for m in teamsWithMaxScore]
        print('teamsWithMaxScoreTeamSize is', teamsWithMaxScoreTeamSize)
        minTeamSize = min(teamsWithMaxScoreTeamSize)
        print('minTeamSize is', minTeamSize)
        teamsWithMaxScoreMinTeamSize = [m for m in range(len(teamsWithMaxScoreTeamSize))
                                        if teamsWithMaxScoreTeamSize[m] == minTeamSize]  # 0-indexed
        print('teamsWithMaxScoreMinTeamSize is', teamsWithMaxScoreMinTeamSize)
        if len(teamsWithMaxScoreMinTeamSize) == 1:
            print(teamsWithMaxScore[teamsWithMaxScoreMinTeamSize[0]] + 1, ' is the winner')
        else:
            print('Team with lowest index is the winner')
            print(teamsWithMaxScore[teamsWithMaxScoreMinTeamSize[0]] + 1, 'is the winner')
    print('-'*50)
    t -= 1

"""
1
5 enidfdcvm
jsficjufg
lf
jsficjuf
jsficjufg
uewqvkwy
"""