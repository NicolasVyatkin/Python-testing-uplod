# Lesson 017-18 Working with modules. Part 1-2

import hello  # impo
import math
import random
from mod import some

from mod import math # can replace, for example, PI with the value specified in the file

hello.some()
print(math.pi)
r = random.randrange(0, 200)  # creates a random number
print(r)

# creating a unique user
user = "User"
user_random = user + str(r)
print(user_random)

some.sum(20,25)
some.sub(15,18)
