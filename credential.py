from user import User

class Credential:
    '''
    A class that create new credential
    '''

    credential_list = []

    def save_credential(self):

        '''
        a method to add new credential
        '''

        save_credential.credential_list.append(self)

    def delete_credential(self):
        '''
        a method to remove credential from credential_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        a method to diplay all credentials saved
        '''

        return cls.credential_list

    @classmethod    
    def find_by_account_name(cls, account_name):
        '''
        a method to find credential of a given account_name
        Args:
            account_name: account name of a credential to search
        Returns:
            Credential that matched the account_name
        '''

        for cred in cls.credential_list:
            if cred.account_name == account_name:
                return cred

    @classmethod
    def is_credential_exists(cls, account_name):
        '''
        A method to check if a credential of a given account name exists
        Args:
            account_name = account name of a credential to check
        Returns:
            Boolean
        '''

        for cred in cls.credential_list:
            if cred.account_name == account_name:
                return True
        return False

def __init__(self, account_name, password):

        self.account_name = account_name
        self.password = password