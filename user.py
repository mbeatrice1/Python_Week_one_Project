
class User:
    """
    Class that generates new instances of contacts.
    """

user_list=[]   

def save_user(self):

    '''
    method to add new user in a system
    '''
 
    User.user_list.append(self)


def delete_user(self):
        '''
        method that remove a user from the list
        '''

        User.user_list.remove(self)

    
@classmethod
def find_by_name(cls, name):
        '''
        Method that find a user by name
        Args:
            name: Name of the user to search for
        Returns:
            User object that matched the name
        '''

        for user in cls.user_list:
            if user.fname == name:
                return user

    
@classmethod
def is_user_exists(cls, name):
        '''
        Method that check if the user exists
        Args:
            name: Name of the user
        Returns:
            Boolean value
        '''

        for user in cls.user_list:
            if user.fname == name:
                return True
        
        return False
    
@classmethod
def display_users(cls):
        '''
        Method that show all users in the user_list
        '''

        return cls.user_list


def __init__(self,lname,fname,password,confirmPassword):
  self.lname=lname
  self.fname=fname
  self.password=password
  self.confirmPassword=confirmPassword
