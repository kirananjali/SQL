#!/usr/bin/env python
# coding: utf-8

# PYHTON

# In[4]:


print("HELLO")


# In[2]:


#TYPE CASTING
#Implicit conversions
a = 5 #(int)
b = 5.20 #(float)
#Explicit conversions
print(str(a+b))


# In[5]:


#BOOLEAN
print(10==9)
print(10>7)
print(10<44)


# In[7]:


# a = 'He's here' # it takes first closing quote as ending of string
a = "He's here."
b = '''it's "here"'''
c = 'He\'s here'


# In[8]:


print(c)


# In[9]:


a = 10
a = 44
print(a)


# ######OPERATIONS

# In[10]:


#ARITHMETIC OPERATIONS
# +,-,*,/,%,**,//
x = 10
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y) #DIVISION RETURNS FLOAT
print(x % y) #MODULUS LEAVES REMINDER
print(x ** y)
print(x // y) #FLOOR DIVION RETURNS INTEGER


# In[11]:


# COMPARISION OPERATORS
# ==, !=,>,<,<=,>=
x = 10
y = 4

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)


# In[13]:


# LOGICAL OPERATIONS
a = True
b = False
print(a and b)
print(a or b)


# In[14]:


q = 6
print(q>5 and q<8)
print(q>5 and q<4)
print(q>9 or q<8)


# In[17]:


#assignment OPERAORS
x = +5
x += 5 #x=x+5
x


# In[18]:


# iNSTEAD OF HARDCODING,WE USE (USER_INPUT)
a = int(input("Enter number1: "))
b = int(input("Enter number2: "))
print(a+b)


# In[19]:


#f string
age = 23
type(age)
year = 2002
x = f"I'm {age} years old, born in {year}"
x


# In[21]:


# .format
student = "Alex"
state = "ohio"
y = f"{student} is from {state} "
y


# In[23]:


#Branching(if/elif/else)
i=4
if(i<3):
    print('less than 3')
    if i<2:
        print('less than 2 and 3') #nested if
elif  i<5:
    print('medium')
elif i<8:
    print('high')
else:
    print('8 or more')


# In[25]:


#LOOPS
#for loop: to repeat an operation no.of times.
#(iterate over thesequence, it continues till it reach last item in sequence.)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# In[26]:


for x in "kiran":  # (for x in) --> this rely on data.
    print(x)


# In[27]:


char = [2,4,6,8,1,3,5,7]
for i in range(len(char)):  # (for i in range()) --> this rely on indexes.
    print(f"index{i} has value {char[i]}")


# In[29]:


x = [1,2,3,4,5,6]
total = 0
for i in range(0, len(x)):
    total += x[i]
total    


# In[30]:


s = 'kiran'
for i in range(len(s)):
    print(i)
    print(s[i])


# In[32]:


#Reverse_string
a = 'bhumi'
x=''
for i in range(len(a)):
    x = a[i] + x
x


# In[ ]:




