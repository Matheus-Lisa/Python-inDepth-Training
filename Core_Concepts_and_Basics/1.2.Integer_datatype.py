#Integer is data type used to represent whole numbers—positive, negative, 
# or zero—without any fractional or decimal part
#example bellow:

var_integer = 12

#The datatype has many operations 

1. Arithmetic Operations
These are basic mathematical operations.

Operator	Operation	                Example	  Result
    +	    Addition	                 5 + 3	    8
    -	    Subtraction	                 5 - 3	    2
    *	    Multiplication	             5 * 3	    15
    /	    Division (floating-point)	 5 / 2	    2.5
    //	    Floor Division (integer)	 5 // 2	    2
    %	    Modulus (remainder)	         5 % 2	    1
    **	    Exponentiation (power)	     5 ** 2	    25
    
2. Relational (Comparison) Operations
These return a boolean (True or False) value based on comparison.

Operator	Operation	       Example	 Result
==	         Equal to	        5 == 5	  True
!=	         Not equal to	    5 != 3	  True
>	         Greater than	    5 > 3	  True
<	         Less than	        5 < 3	  False
>=	         Greater or equal   5 >= 5	  True
<=	         Less or equal	    5 <= 6	  True

3. Bitwise Operations
These operate on the binary representation of integers.

Operator	Operation	    Example	  Result
&	           AND	         5 & 3      1
`	            `	          OR	   `5
^	           XOR	         5 ^ 3	    6
~	           NOT (invert)	  ~5	   -6
<<	           Left shift	 5 << 1	    10
>>	           Right shift	 5 >> 1	    2

4. Assignment Operations (with integers)
Used to assign values to variables, with combined arithmetic operations.

Operator	Operation	                Example	        Equivalent
=	        Assignment	                 x = 5	          x = 5
+=	        Add and assign	             x += 3	          x = x + 3
-=	        Subtract and assign	         x -= 2	          x = x - 2
*=	        Multiply and assign	         x *= 2	          x = x * 2
/=	        Divide and assign	         x /= 2	          x = x / 2
//=	        Floor divide and assign	     x //= 2	      x = x // 2
%=	        Modulus and assign	         x %= 2	          x = x % 2
**=	        Exponent and assign	         x **= 2	      x = x ** 2
&=	        Bitwise AND and assign	     x &= 2	          x = x & 2
`	                =`	            Bitwise OR and assign    `x
^=	        Bitwise XOR and assign	     x ^= 2	          x = x ^ 2
<<=	        Left shift and assign	     x <<= 1	      x = x << 1
>>=	        Right shift and assign	     x >>= 1	      x = x >> 1

5. Logical Operations
These can involve integers, where non-zero values are considered True.

Operator	Operation	  Example	            Result
and	         Logical       AND 5 > 3 and 3 > 2	 True
or	         Logical       OR 5 > 3 or 3 < 2     True
not	         Logical       NOT not (5 > 3)	     False

