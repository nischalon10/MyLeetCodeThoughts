The first instinct that came to my mind was to write down all the possible ways for each value of n to observe a pattern.

`n=1 => (1)                                                                          = 1`<br>
`n=2 => (1,1) (2)                                                                    = 2`<br>
`n=3 => (1,1,1) (1,2) (2,1)                                                          = 3`<br>
`n=4 => (1,1,1,1) (1,1,2) (1,2,1) (2,1,1) (2,2)                                      = 5`<br>
`n=5 => (1,1,1,1,1) (1,1,1,2) (1,1,2,1) (1,2,1,1) (2,1,1,1) (1,2,2) (2,1,2) (2,2,1)  = 8`<br>

Clearly the pattern seemed like fibonacci numbers, but why

###Since it is fibonacci it is recursive, but how ?

So for each lets say the there are n steps, and if the first step is
a single = there are only a spesific number of ways it can traverse through the n-1 steps 
a double = there are only a spesific number of ways it can traverse through the n-2 steps 

so the possible ways you can climb up is the sum of different ways you can go up if there were n-1 steps and n-2 steps
hence the recursion.

From here on converting this to a iterative function to match the time contraint was simple ;)