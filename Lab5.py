#!/usr/bin/env python
# coding: utf-8

# In[4]:


##Ask user to input password
aevans_pass = str(input("Enter password"))

if str(aevans_pass) == 'angelina23':
    print("Welcome Angelina Evans")
else:
    print("Please contact 1-800-768-9088 for password assistance!")


# In[7]:


## Tells user that 2164 is a leap year
year = 2164

rule1 = year%4==0
print(rule1)

rule2 = year%100==0

exclude_exception = year%100!=0 or year%400==0
print(rule2)

if (rule1) and (exclude_exception):
    print("You entered a leap year")

else:
    print('The year you entered is not a leap year')


# In[22]:


grade = int(input("Please enter a grade!"))

if int(grade) <= 59 and grade >= 0:
    print("You got an E")
if int(grade) <= 63 and grade >= 60:
    print("You got a D-")
if int(grade) <= 66 and grade >= 64:
    print("You got a D")
if int(grade) <= 69 and grade >= 67:
    print("You got a D+")
if int(grade) <= 72 and grade >= 70:
    print("You got a C-")
if int(grade) <= 75 and grade >= 73:
    print("You got a C")
if int(grade) <= 78 and grade >= 76:
    print("You got a C+")
if int(grade) <= 81 and grade >= 79:
    print("You got a B-")
if int(grade) <= 84 and grade >= 82:
    print("You got a B")
if int(grade) <= 88 and grade >= 85:
    print("You got a B+")
if int(grade) <= 93 and grade >= 89:
    print("You got a A-")
if int(grade) <= 100 and grade >= 94:
    print("You got a A")


# In[11]:


##Create program to generate NET IDs
import random

random_digits = random.randint(100000, 999999)

net_id = str(input("Please provide your first and last initial so that we may generate a Net ID for you!"))
print(net_id + str(random_digits))


# In[16]:


## Create an example 

questions = {'2','5'}
correct_answer = 2

your_answer = str(input('Which of these are an even number?'))

if correct_answer == 2:
    print('That is the correct answer, youre so smart!')
else:
    print('Try again!')


# In[ ]:




