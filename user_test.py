import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test Class to test all the functionality of user class.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases.
    '''

    def setUp(self):
        '''
        Set up method to run before each test classes.
        '''

        self.new_user = User("Beatrice","Uwamahoro","password","password")

    def tearDown(self):
        '''
        Test case that run after each test case
        '''

        User.user_list = []

    def test_init(self):
        '''
        test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.fname, "Beatrice")
        self.assertEqual(self.new_user.lname, "Uwamahoro")
        self.assertEqual(self.new_user.password, "password")
        self.assertEqual(self.new_user.confirmPassword, "password")


    def test_save_user(self):
        '''
        Test case to test if the user is saved into the list
        '''

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_delete_user(self):
        '''
        Test case to test if the user object is deleted
        '''

        self.new_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 0)

    def test_find_by_name(self):
        '''
        Test case that test if we can find a user by name
        '''

        self.new_user.save_user()
        found_user = User.find_by_name("Beatrice")
        self.assertEqual(found_user.lname, self.new_user.lname)

    def test_is_user_exists(self):
        '''
        Test case that test if the user of a given name exist
        '''

        self.new_user.save_user()
        self.assertTrue(User.is_user_exists("Beatrice"))

    def test_display_users(self):
        '''
        Test case to test if we can display all users from user_list
        '''

        self.new_user.save_user()
        self.test_user = User("Princia", "Pascy", "pass", "pass")
        self.test_user.save_user()
        self.assertEqual(len(User.user_list), 2)


if __name__ == '__main__':
    unittest.main()