# %% [markdown]
# # Homework 2
# 
# ## Your Name Here (or your names here if you are pair programming)
# 
#  - Student Name:
#  - Student UT EID:
# 
# 
#  - Partner Name:
#  - Partner UT EID:
# 
# ## Practicing Pandas
# 

# %%
# Standard Headers
# You are welcome to add additional headers here if you wish
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Enable inline mode for matplotlib so that Jupyter displays graphs
%matplotlib inline

# %% [markdown]
# # Social Network Dataset
# 
# In this assignment we work with a social network dataset. 
# 
# You have 5 tables to work on. 
# 
# 1. **person_knows_person**
# This table represents the friendship between users. A person can have many friends. Persons have unique integer id number. 
# 
# 2. **person_likes_post_file** 
# This tables represents user likes. A person and a post is represented by IDs. 
# 
# 3. **post_hasCreator_person**
# A person creates many posts. Each post has a unique creator person id. 
# 
# 4. **comment_replyOf_post**
# This table represents comments on posts. Both post and comments have unique ids. 
# 
# 5. **comment_hasCreator_person** 
# A user can comment on posts. Each comment has a unique creator person id. 
# 

# %%
url = "https://raw.githubusercontent.com/kiat/Elements-of-Data-Analytics/main/datasets/social-media/"

person_knows_person_file = url + "person_knows_person.csv"
person_likes_post_file = url + "person_likes_post.csv"
post_hasCreator_person_file = url + "post_hasCreator_person.csv"
comment_replyOf_post_file = url + "comment_replyOf_post.csv"
comment_hasCreator_person_file = url + "comment_hasCreator_person.csv"

person_knows_person = pd.read_csv(person_knows_person_file,  sep='|')
person_likes_post = pd.read_csv(person_likes_post_file,  sep='|')
post_hasCreator_person = pd.read_csv(post_hasCreator_person_file,  sep='|')
comment_replyOf_post = pd.read_csv(comment_replyOf_post_file, sep='|')
comment_hasCreator_person = pd.read_csv(comment_hasCreator_person_file,  sep='|')

print(person_knows_person.head(5))
print("-------------------------")

print(person_likes_post.head(5))
print("-------------------------")

print(post_hasCreator_person.head(5))
print("-------------------------")

print(comment_replyOf_post.head(5))
print("-------------------------")

print(comment_hasCreator_person.head(5))
print("-------------------------")

# %% [markdown]
# # Question - 1. Who are the top-10 users who have the highest number of friends? (4 points)
# Count up the number of friends of each user and provide the top-10 of this number of friend count list. Print out their user IDs. 

# %%
# Code here

# %% [markdown]
# # Question - 2. Who wrote the most liked post?  (4 points)
# Count up the number of likes for each post and find out who wrote that post. 
# Print out the user id. If there are multiple maximum print them all. 

# %%
# Code here 

# %% [markdown]
# # Question - 3. Who wrote the most influential post? The most influential post is the most discussed and most liked post. (4 points)
# 
# **Tip:** First, count up the number of comments and likes that each post has. Then find out which post it is, and finally find out who wrote that. 
# Print out one user id. 
# If there is a tie, print out the ***one***  at the tope of the list.
# 

# %%
# Code here 

# %% [markdown]
# # Question - 4. Create two histograms for the distributions of the number of likes and comments that users have created. (4 points)
# Describe the shape of these data two data distributions. 
# 
# **Tip:** First perpare two lists of number of likes and number of comments that users have done. You need to count up how many likes and how many comments each unique user id has. 

# %%
# Code here

# %% [markdown]
# # Question - 5. What is the Pearson correlation coefficient between the number of comments and the number of likes that users do on the social network? (4 points)
# 
# Print out one number. 
# 
# 
# 
# **Tip:** You can calculate correlation coefficient using the following formula: 
# Assume that x and y are two arrays of data, in this case number of likes and comments of each user. n is the number of users. 
# 
# **Bonus Tip:** Consider that some users might have liked posts, but not liked any comments, or vice versa.
# 
# You can use whichever technique you would like for the question, as long as it has been discussed in lecture.
# 
#  
# 
# 
# \begin{align*}
# r= {{ n(\sum x y ) - (\sum x ) (\sum y)    } \over { \sqrt{ [ n \sum x^2  -
# (\sum x)^2 ] [ n\sum y^2 - (\sum y )^2 ] } } }
# \end{align*}
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# %%
# Code here


