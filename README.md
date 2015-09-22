# 8-tile-problem-a-star<br>
`8 tile` problem using `A * search` and `Manhattan distance` as heuristic function<br>
<br>
8 tile problem is a famous problem in artificial intelligence (AI). In this problem, a 3x3 grid is given containing the numbers 1-8 and a blank tile. There are specific rules to move a blank tile and only operation available is to swap the blank tile with any of it's 4 possible neighbours.<br>
<br>
We have to find sequence of actions performed on the blank tile so as to get a sorted form as follows:-<br>
[[1 2 3]<br>
[4 5 6]<br>
[7 8 'B']]<br>
Here 'B' depicts the blank tile.<br>
<br>
This program solves this problem using A * search technique with Manhattan distance as heuristic function. For more information, visit `https://en.wikipedia.org/wiki/A*_search_algorithm`.
