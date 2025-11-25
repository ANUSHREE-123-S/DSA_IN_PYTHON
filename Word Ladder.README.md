📝 Problem Summary

You are given:

A beginWord

An endWord

A list of valid words (wordList)

You need to find the shortest transformation sequence from beginWord to endWord, where:

Only one letter can be changed at a time.

Each transformed word must exist in wordList.

Every transformation counts as 1 step.

If no transformation is possible, return 0.

🎯 Key Insight

This is a shortest path problem → solved using Breadth-First Search (BFS).

Important Observations

Changing one letter at a time forms patterns like:
"hot" → "*ot", "h*t", "ho*"

Words sharing a pattern are neighbors (one-letter apart).

We precompute these patterns to make BFS fast.

🧠 Approach
1️⃣ Preprocessing — Build Pattern Dictionary

For each word and each position, replace one character with "*".

Example: "dog"
Patterns: "*og", "d*g", "do*"

We store all such patterns in a dictionary:

pattern → list of words


This helps us instantly find all one-step neighbors.

2️⃣ BFS from beginWord

Use queue: (current_word, level)

Steps:

Start with (beginWord, 1)

For each pattern of current_word:

Check all neighbors

If neighbor is endWord → return level + 1

Otherwise push into queue

Mark visited words

Clear pattern list after using it (to avoid revisiting)

⏱️ Time & Space Complexity
Part	Complexity
Preprocessing patterns	O(N × L)
BFS	O(N × L)
Total	O(N × L)
Where:	

N = number of words

L = word length

Space complexity = O(N × L) for storing patterns and BFS queue.
