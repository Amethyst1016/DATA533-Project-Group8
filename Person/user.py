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
        
        # function to see if username exists already
    def exist(self):
        otheruser = input("Please enter a username to see if it already exists")
        for i in users:
            if self.user == otheruser:
                return "This username exists."
        else:
            return "This username does not exists. Please create an account."
        
        # change password
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value


# Creating database of users

user1 = User('madison13g', 'password1')
user2 = User('amethyst1016', 'password2')
user3 = User('khaladhasan', 'khalad1')
user4 = User('jeffandrews', 'jeff1')
user5 = User('christeldeas', 'christel1')
user6 = User('gemarodriguezperez', 'gema1')
user7 = User('ifeomaadaji', 'ifeoma1')
user8 = User('johnthompson', 'john1')
user9 = User('emeliegustafsson', 'emelie1')
user10 = User('patricialassere', 'patricia1')



