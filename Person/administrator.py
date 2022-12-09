#!/usr/bin/env python
# coding: utf-8

# In[10]:


import user
import post   


class Admin(User):
    def __init__(self, user, password, admincode):
        User.__init__(self, user, password)
        self.admincode = admincode
        
    def displayUser(self):
        User.displayUser(self)
        print('Username: {}, Admin code: {}'.format(self.user, self.admincode))
        
    # check number of users
    def displayCount(self):
        print("Total Users %d" % User.userCount)
    
    # delete any user
    def __del__(self, other):  # admin can do del ObjectName and it will print 'deleted'
        print("{} deleted a user with username: {}".format(self.user, other.user))  
    
    # search for flagged content in posts (must have from post import post)
    def searchFlagInPost(self, flagged_keyword):
        for post in Post:
            if flagged_keyword in post:
                post.show()
    
    # print list of current users
    def userlist(self):
        for i in users:
            print("Username of user {} is: {}".format([i], self.user))


# In[ ]:





# In[ ]:




