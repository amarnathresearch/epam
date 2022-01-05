class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def setDesignation(self, designation):
        self.designation = designation
    
    def getUserName(self):
        return f'{self.firstname} {self.lastname}'
    def getDesignation(self):
        return f'{self.designation}'
    

# user = User('micheal', 'rob')

# print(user.getUserName())