
from user import User

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


# Creating database of admins

admin1 = Admin('Dan', 'password3', 'A1')
admin2 = Admin('Amethyst', 'password4', 'A2')
admin3 = Admin('Madison', 'password5', 'A3')
admin4 = Admin('Abigail', 'password6', 'A4')
admin5 = Admin('Linda', 'password7', 'A5')
admin6 = Admin('Tom', 'password8', 'A6')



