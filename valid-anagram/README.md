This is a simple question. The idea was simple and there were multiple ways to solve it.

1. Use a hashmacp to store the number of letters and their types in each word
2. use an array like hashmap(switches) but instead of comparing two arrays use just one and add numbers to track the first word's letters and subtract numbers to track the second word's numbers. If it is an array where all the elements were same as before, the words are anagrams
3. Sort the two strings and compare them, if same they are anagrams
   
The 3rd solution seems to be the most elegant one. The only extra space required will be whatever the sorting algorithm uses but once it is done the space is freed up.