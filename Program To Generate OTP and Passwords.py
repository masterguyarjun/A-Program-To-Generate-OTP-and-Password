# A Program To Generate OTP and Password

# 6 Digit number to be used as OTP

from random import *

for i in range (2):
    print ( randint ( 0, 9 ), randint ( 0, 9 ), randint ( 0, 9 ), randint ( 0, 9 ), randint ( 0, 9 ), randint ( 0, 9 ),
            sep='' )

# another example

otp = ''
for i in range(6):
    otp = otp + str(randint(0, 9))
print(otp)

# Program To Generate Random Password:

from random import *

alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
for i in range(10):
    print(choice(alphabets), choice(digits), choice(alphabets), choice(digits), choice(alphabets), choice(digits), sep = '')