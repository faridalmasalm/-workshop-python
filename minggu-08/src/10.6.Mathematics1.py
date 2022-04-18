import random
random.choice(['apple', 'pear', 'banana'])
# 'apple'  (Output)
random.sample(range(100), 10)   # sampling without replacement
# [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]  (Output)
random.random()    # random float
# 0.17970987693706186  (Output)
random.randrange(6)    # random integer chosen from range(6)
# 4  (Output)