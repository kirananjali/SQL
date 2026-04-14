#!/usr/bin/env python
# coding: utf-8

# Right-Angled Triangle
# *
# **
# ***
# ****
# *****

# In[1]:


#for loop
n = 5

for i in range(1, n+1):
    print("*" * i)


# In[2]:


#while loop
n = 5
i = 1

while i <= n:
    print("*" * i)
    i += 1


# Right-Angled Triangle(Decreasing)
# *****
# ****
# ***
# **
# *

# In[3]:


#for loop
n = 5

for i in range(n, 0, -1):
    print("*" * i)


# In[4]:


#while loop
n = 5
i = n

while i > 0:
    print("*" * i)
    i -= 1


# Left-Aligned Triangle
#     *
#    **
#   ***
#  ****
# *****

# In[5]:


#for loop
n = 5

for i in range(1, n+1):
    print(" " * (n - i) + "*" * i)


# In[6]:


#while loop
n = 5
i = 1

while i <= n:
    print(" " * (n - i) + "*" * i)
    i += 1


# Number Triangle
# 1
# 12
# 123
# 1234
# 12345

# In[7]:


#for loop
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# In[8]:


#while loop
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1


# Floyd’s Triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# In[9]:


#for loop
n = 4
num = 1

for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()


# In[10]:


#while loop
n = 4
i = 1
num = 1

while i <= n:
    j = 1
    while j <= i:
        print(num, end=" ")
        num += 1
        j += 1
    print()
    i += 1


# In[ ]:




