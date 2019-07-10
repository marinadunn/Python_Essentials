"""
Created by Marina Dunn on 7/8/19
Last edited: 7/8/19
Goal: Based on hypothesis of Lothar Collatz:
a) for any non-negative and non-zero integer, call it c0
b) if even, evaluate a new c0 as c0/2
c) if odd, evaluate new c0 as 3 * c0 + 1
d) if c0 != 1, skip to point b)
Theoretically that regardless of c0 initial value, will always go to 1.
Reads in number from user and evaluates as long as c0 isn't 1, outputs c0 values.
Based on Python Institute practice code
"""

#Reads in initial c0 value and turns it into an integer value
c0 = int(input("Enter a number c0:"))

if c0 > 1:						#non-negative
	steps = 0
	while c0 != 1:
		if c0 % 2 != 0: 		#if odd
			c0_new = 3 * c0 + 1
		else:
			c0_new = c0 // 2 	#integer division
		print(c0) 				#prints intermediate values of c0 too
		c0 = c0_new 			#updates c0
		steps += 1 				#continue increasing steps
	print("steps = ", steps) 	#prints how many steps were taken when evaluating
else:
	print("Bad c0 value:")
         
