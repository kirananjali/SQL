#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=10
sum=0
i=1
while i<=n:
    sum = sum + i
    i=i+1 #Update counter
print("the sum is:",sum)


# In[2]:


count = 5
while count >= 0:
    print("Countdown:",count)
    count -=1
print("Happy New Year")


# BREAK
# When condition is met, it breaks the loop(come out of loop)

# In[3]:


name = 'stop'
while True:
    user_input = input("enter the name:")
    if user_input == name:
        print("name match, break")
        break
    else:
        print("name didn't matched, keep trying")


# CONTINUE
# used to skip the condition

# In[ ]:





# STRINGS AND LISTS
# new line -> \n

# In[5]:


len('hello')


# In[6]:


len('hi bro') #space counts


# In[7]:


s='hello world'  #s[start:stop:step]


# In[8]:


s[0]


# In[9]:


s[0:] #starts with 0 goes till end


# In[10]:


s[:5] #starts with 0th index, ends at 4th 'index'


# In[11]:


s[:] #gets entire assigned word/statement


# In[12]:


s[-5] # negative indexing starts with -1 not 0


# In[13]:


s[::3] # HelLo WorLd, step 3(0,1,2 indexes), h(0) [e1l2] l(0) (o1_2)..


# In[14]:


s[::-1] #reversing


# STRING PROPERTIES
# Immutable( Can't be changed once assigned)

# In[15]:


s='hello'
s[0]


# In[16]:


s[0]=q #can't reassign


# In[18]:


s + ',how are you' # but can append new string to existing string


# BUILT-IN STRING FUNCTIONS

# In[20]:


s = 'hello world'
s.upper()


# In[22]:


s.lower()


# In[23]:


s.split() 

#The split() method splits a string into a list.

#You can specify the separator, default separator is any whitespace.
# It removes the seperator from the resulting substring


# In[25]:


s.split('w')


# In[27]:


a = 'A@B@C@D'
a.split('@')


# In[28]:


## setting the maxsplit parameter to 1, will return a list with 2 elements.
a.split('@',1)


# LOCATION AND COUNTING

# In[33]:


s = 'hello world'
s.count('world') #no of times that particulat letter/word comes in the sentence


# In[35]:


s.find('o') # location of 'o' that came first, we can use loop to know other occurances as well


# In[37]:


#tab spacing
print('hello\thaiiii') 


# In[38]:


#next line
print('hello\nhaiiii')


# ISCHECK METHOD

# In[39]:


s = 'hello02'


# In[40]:


s.isalnum() #is alphanumeric?


# In[45]:


print(s.islower())
print(s.isspace()) #Check if all the characters in the text are whitespaces
print(s.istitle()) # 1st letter should be CAPITAL
print(s.endswith('2'))


# SPLIT METHOD, SKIPS THE SEPERATOR
# PARTITION
# The partition() method searches for a specified string, and splits the string into a tuple containing three elements.
# 
# The first element contains the part before the specified string.
# 
# The second element contains the specified string.
# 
# The third element contains the part after the string.

# In[47]:


w = 'they are here'
w.partition('they')


# In[ ]:


#If the specified value is not found, the partition() method returns a 
#tuple containing: 
#   1 - the whole string, 
#    2 - an empty string, 
 #   3 - an empty string:


# In[48]:


w.partition('not')


# LISTS (It can store any datatype, any no of data points)

# In[57]:


l1 = [1,2,3]
l2 = ['hello',1,2.2,'hi']


# In[50]:


len(l1)


# In[52]:


#indexing slicing
l2[2]


# In[53]:


l2[1:]


# In[54]:


l1+ ['come',77]


# In[58]:


#METHODS
#APPEND
l1.append('append me!!')
l1


# In[59]:


#POP -> Last in 1st out
l1


# In[60]:


l1.pop()


# In[62]:


#to store popped item, it should be assigned somewhere

popped_item = l2.pop()
popped_item


# In[64]:


new_lst = ['k','i','r','a','n']
new_lst.reverse()
new_lst


# In[67]:


new_lst.sort()
new_lst


# In[69]:


#NESTED LIST
a1 = [1,2]
a2 = [3,4]
matrix = [a1,a2]
matrix


# In[70]:


matrix [1][1]


# In[71]:


matrix [0]


# LIST COMPREHENSIONS
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# 

# In[ ]:


#SYNTAX
#newlist = [expression for item in iterable if condition == True]


# In[74]:


fruits = ["grapes", "banana", "oranges", "sapota", "mango"]

newlist = [x for x in fruits if "o" in x]

print(newlist)


# In[76]:


newlist = [x for x in fruits if x != "oranges"]
newlist


# In[78]:


newlist = [x for x in range(8)]
newlist


# In[80]:


newlist = [x for x in range(10) if x<4]
newlist


# In[81]:


newlist = [x.upper() for x in fruits]
newlist


# In[82]:


newlist = ['python' for x in fruits]
newlist


# In[84]:


fruits = ["grapes", "banana", "oranges", "sapota", "mango"]
newlist = [x if x!='grapes' else 'berries' for x in fruits] #Return the item if it is not grapes, if it is banana return berries
newlist


# In[93]:


#APPEND, EXTEND
x = [1,2,3]
x.append([4,5])
x


# In[94]:


x.extend([8,9])
x


# In[95]:


x.pop()
x


# In[96]:


x


# In[103]:


z = [1,2,3,4]
z.remove(3) # want to explicitly remove something
z


# In[ ]:




