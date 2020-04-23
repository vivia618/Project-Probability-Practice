# # Coin Flips and Die Rolls
# Use NumPy to create simulations and compute proportions for the following outcomes. The first one is done for you.
# **Please note again that we are using 0 to represent heads, and 1 to represent tails.**
# import numpy
import numpy as np

# ### 1. Two fair coin flips produce exactly two heads
# simulate 1 million tests of two fair coin flips
tests = np.random.randint(2, size=(int(1e6), 2))

# sums of all tests
test_sums = tests.sum(axis=1)

# proportion of tests that produced exactly two heads
print((test_sums == 0).mean())


# ### 2. Three fair coin flips produce exactly one head
# simulate 1 million tests of three fair coin flips
tests = np.random.randint(2, size = (int(1e6), 3))

# sums of all tests
test_sums = tests.sum(axis = 1)

# proportion of tests that produced exactly one head
print((test_sums == 1).mean())

# ### 3. Three biased coin flips with P(H) = 0.6 produce exactly one head
# simulate 1 million tests of three biased coin flips
# hint: use np.random.choice()
tests = np.random.choice(2,size =(int(1e6), 3), p = [0.6,0.4])

# sums of all tests
test_sums = tests.sum(axis = 1)

# proportion of tests that produced exactly one head
print((test_sums == 1).mean())

# ### 4. A die rolls an even number
# simulate 1 million tests of one die roll
tests = np.random.randint(1,7, size = int(1e6))

# proportion of tests that produced an even number
print((tests % 2 == 0).mean())

# ### 5. Two dice roll a double
# simulate the first million die rolls
first = np.random.randint(1,7, size = int(1e6))

# simulate the second million die rolls
second = np.random.randint(1,7, size = int(1e6))

# proportion of tests where the 1st and 2nd die rolled the same number
print((first != second).mean())