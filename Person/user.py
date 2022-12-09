#!/usr/bin/env python
# coding: utf-8

# In[54]:


class User():
    
    #counter
    userCount = 0 
    
    # store all current users
    users = [] 
    
    def __init__(self, user, password):
        self.user = user
        self._password = password # password is private 
        #print('Username: {}'.format(self.user))
        User.userCount += 1
        if user not in self.users:
            self.users.append(self)
        
    def displayUser(self):
        print('Username: {}'.format(self.user))
    
        # login prompt when opening the package
        
        # function to create new account (as selected option in prompt if no username & pw existing)
        
        # change password
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value


# In[ ]:




