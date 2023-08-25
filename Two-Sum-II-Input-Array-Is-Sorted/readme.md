The approach I took to solve this problem was inspired from the neet code video I saw for the valid palindrome problem. 
In this problem I realized I could eliminate unwanted iterations using some logic.
The approach here was to use the sorted feature of the list to my advantage, I got two pointers, one on each side. I iterated through the list from both ends and moved the pointer that has the largest value only if the smallest value moved over the larger pointer.
This was fairly simple to impliment and easy to visualize also!