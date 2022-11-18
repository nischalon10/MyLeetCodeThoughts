Starting today, as I work towards practicing problem solving skills from neetcode.io I will be posting my learning here.

This was a easy yet tricky question. I thought the answer is very simple use two pointers and iterate through every element however this exceeded the time limit. 

Starting to understand space and time complexity gradually, My approach had a time complexity of O(n^2).

There were 2 major ways how I could accomplish the optimization needed.
1. Sort the array (so that you only need to compare any two adjacent elemnts only to solve the problem)
2. Use another list to keep track all the lements already iterated to see if we encounter another element of similar kind

I chose to solve it using the 2nd method but the 1st one seems pretty optimized too
