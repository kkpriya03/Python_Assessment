
1. What is the output of the following code?
a = 5 
b = 10 
print(a < b < 20)
print((a<b)and(b<20))
print((5<10) and (10<20))
output:True

 2. Predict the output: 
x = True
 y = False
 print(x + y * x)
true=1
false=0
print(1+0*1)
output=1

3. What does this expression evaluate to? 
print(4 ** 0 ** 2)
4 ** (0 ** 2)
4 ** 0
Output:1

4. Find the result of this bitwise operation:
a = 12 
b = 5
 print(a ^ b)
*canulate the binary of a and b values:
12->  binary  is :1 1 0 0
5-> binary is :1 0 1
This is XOR agar dono value same h to false hoga
1 1 0 0
0 1 0 1
Ans is: 1 0 0 1
Canculate in numeric: 1 0 0 1
			8 4 2 1
			8 0 0 1
Ans is:8+1=9
Output is: 9

5. Guess the output:
print((3 and 0) or (0 and 3))
((0) or (0))
Output is:0

6. What's the output of this tricky comparison?
print(256 is 256)
print(257 is 257)
output is:True

7. Evaluate this expression:
a = 7
print(~a + 1)
~a=-(a+1)
=-(7+1)
Print(~a + 1)
=-8+1
Output is:-7

8. What will this print?
a = True 
b = False
 print((a or b) and not (a and b))
((true or false) and (not(true and false)))
((true) and (not(false)))
((true) and (true))
Output is:True

9. What's the output?
 print(10 > 5 == True)
((10>5) and (5==true))
((True) and (false))
Output is: false

10. Evaluate this expression:
print(2 + 3 * 4 ** 2 // 8 % 3)
(2+3*16//8%3)
(2+48//8%3)
(2+6%3)
(2+0)
Output is:2

11. What does this expression evaluate to?
print(1 << 2 + 1)
(2 + 1 = 3)
Print(1<<3)

12. Predict the output:
 a = 3 
b = 2 
a *= b + 1 
print(a)
a*=a*(b+1)
=3(2+1)
=9
Output is:9

13. Evaluate this chained comparison: 
print(3 < 5 > 2 == 2)
(3 < 5) and (5 > 2) and (2 == 2)
((true) and (true) and (true))
Output is:True

14. Guess the result: 
print(10 // 3 * 3 + 1 % 3)
(3*3+1%3)
(9+1%3)
(9+1)=10
Output is:10

15. What is the result of this? 
x = 10
 y = 20 
print(x & y | x ^ y)
((10 & 20)|| (10^20))
10 binary is :	8 4 2 1
			1 0 1	0
20 binary is : 	16 8 4 2 1
1	0 1 0 0

First is (x & y) : 0 1 0 1 0
		        1 0 1 0 0
Ans is 	       :0 0  0 0 0
Second is :  (x^y) means XOR
	Ans is :    1 1 1 1 0
((00000)||(11110))
Final output:30

16. Trick with boolean and bitwise:
    
a = True 
b = False
 print(a & b or a ^ b)
((true & false) or (true^false))
((false) or(true))
True
Output is: true

17. Evaluate this:
x = 8 
print(x >> 1 << 2)
((x>>1)<<2))
(8<<2)
16
Output is : 16

18. What does this produce?
 print(5 + True * False + not False)
(5+0+1)=6	
Output is :6

19. Operator confusion:
 print((not 0) * (False or 1))
((1) *(0 or 1)
(1*1)
Output is :1

20. Mix of precedence and associativity:
print(4 + 3 * 2 ** 2 // 2 - 1)
(4+3*4//2-1)
(4+12//2-1)
(4+6-1)
(10-1)
Output is :9




			
			









"""
