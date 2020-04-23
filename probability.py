#!/usr/bin/env python
# coding: utf-8

# # Coin Flips and Die Rolls
# Use NumPy to create simulations and compute proportions for the following outcomes. The first one is done for you.
# 
# **Please note again that we are using 0 to represent heads, and 1 to represent tails.**

# In[ ]:


# import numpy


# ### 1. Two fair coin flips produce exactly two heads

# In[ ]:


# simulate 1 million tests of two fair coin flips
tests = np.random.randint(2, size=(int(1e6), 2))

# sums of all tests
test_sums = tests.sum(axis=1)

# proportion of tests that produced exactly two heads
(test_sums == 0).mean()


# ### 2. Three fair coin flips produce exactly one head

# In[ ]:


# simulate 1 million tests of three fair coin flips
tests = 

# sums of all tests
test_sums = 

# proportion of tests that produced exactly one head


# ### 3. Three biased coin flips with P(H) = 0.6 produce exactly one head

# In[ ]:


# simulate 1 million tests of three biased coin flips
# hint: use np.random.choice()
tests = 

# sums of all tests
test_sums = 

# proportion of tests that produced exactly one head


# ### 4. A die rolls an even number

# In[ ]:


# simulate 1 million tests of one die roll
tests = 

# proportion of tests that produced an even number


# ### 5. Two dice roll a double

# In[ ]:


# simulate the first million die rolls
first = 

# simulate the second million die rolls
second = 

# proportion of tests where the 1st and 2nd die rolled the same number

