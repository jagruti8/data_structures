# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 04:18:54 2020

@author: JAGRUTI
"""

# define Group class, having a name, subgroups and users
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        
    # adding a group
    def add_group(self, group):
        self.groups.append(group)

    # adding a user
    def add_user(self, user):
        self.users.append(user)

    # accessing the groups
    def get_groups(self):
        return self.groups

    # accessing the users
    def get_users(self):
        return self.users

    # getting name of the group
    def get_name(self):
        return self.name

# check if user is present in the group
def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    # if no user name is given
    if user == "" or user == None:
        print("Invalid user name. Please enter valid user name")
        return None, None
    
    # set answer to False and raise to True after finding the user
    answer = False
    # to save path for user starting from the group
    path = ""
    
    # if user is present in the group
    if user in group.users:
        answer = True
        path = group.name + "----->" + user
        return path, answer
    
    # if group has sub-groups traverse the subgroup to find the user
    for subgroup in group.groups:
        path, answer = is_user_in_group(user, subgroup)
        # if user is found in a particular subgroup, break from the loop
        if answer == True:
            path = group.name + "----->" + path
            break
    
    # if user is not present in the group
    if path == "":
        path = "Sorry not found"
        
    return path, answer

## Test Cases
    
## Example 1
    
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

path, answer = is_user_in_group("sub_child_user", parent)
print(path)   # parent----->child----->subchild----->sub_child_user
print(answer) # True

path, answer = is_user_in_group("", parent)
print(path)    # Invalid user name. Please enter valid user name | None
print(answer)  # None

path, answer = is_user_in_group("sub_child_user1", parent)
print(path)   # Sorry not found
print(answer) # False

## Example 2

school = Group("school")
boys = Group("boys")
girls = Group("girls")
primary = Group("primary")
high_school = Group("high_school")

school.add_group(boys)
school.add_group(girls)
school.add_group(primary)
school.add_group(high_school)

sports = Group("sports")
dance = Group("dance")
drama = Group("drama")
games = Group("games")

boys.add_group(sports)
girls.add_group(dance)
primary.add_group(drama)
games.add_group(games)

sports_list = ["cricket", "football", "hockey", "badminton"]
dance_list = ["classical", "bollywood", "hip_hop"]
drama_list = ["Macbeth", "Merchant_of_Venice", "Julius Caesar"]
games_list = ["hide_and_seek", "passing_the_passer"]

for item in sports_list:
    sports.add_user(item)
for item in dance_list:
    dance.add_user(item)
for item in drama_list:
    drama.add_user(item)
for item in games_list:
    games.add_user(item)

path, answer = is_user_in_group("", school)
print(path)    # Invalid user name. Please enter valid user name | None
print(answer)  # None

path, answer = is_user_in_group("Macbeth", school)
print(path)    # school----->primary----->drama----->Macbeth
print(answer)  # True

path, answer = is_user_in_group("Harry_Potter", school)
print(path)    # Sorry not found
print(answer)  # False

path, answer = is_user_in_group("football", boys)
print(path)    # boys----->sports----->football
print(answer)  # True

