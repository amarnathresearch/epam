'''
User Class defined
'''
class User:
    '''
    Class defined
    '''
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def getUser(self):
        '''
        Getting user first name and last name
        '''
        return f'{self.firstname} {self.lastname}'

user = User('siva', 'ram')
print(user.getUser())
