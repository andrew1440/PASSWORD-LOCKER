import unittest
import pyperclip
from user import User, Credential


class TestUser(unittest.TestCase):
    '''
	Test class that defines test cases for the user class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''

    def setUp(self):
        '''
		Function to create a user account before each test
		'''
        self.new_user = User('Andy', 'corona', 'chicken1440')

    def test__init__(self):
        '''
		Test to if check the initialization/creation of user instances is properly done
		'''
        self.assertEqual(self.new_user.first_name, 'Andy')
        self.assertEqual(self.new_user.last_name, 'corona')
        self.assertEqual(self.new_user.password, 'chicken1440')

    def test_save_user(self):
        '''
		Test to check if the new users info is saved into the users list
		'''
        self.new_user.save_user()
        self.assertEqual(len(User.users_list), 1)


class TestCredentials(unittest.TestCase):
    '''
	Test class that defines test cases for the credentials class behaviours.
	Args:
	    unittest.TestCase: helps in creating test cases
	'''

    def test_check_user(self):
        '''
		Function to test whether the login in function check_user works as expected
		'''
        self.new_user = User('Andy', 'corona', 'chicken1440')
        self.new_user.save_user()
        user = User('Andy', 'corona', 'chicken1440')
        user.save_user()

        for user in User.users_list:
            if user.first_name == user.first_name and user.password == user.password:
                current_user = user.first_name
        return current_user

        self.assertEqual(current_user, Credential.check_user(user.password, user.first_name))

    def setUp(self):
        '''
		Function to create an account's credentials before each test
		'''
        self.new_credential = Credential('Andy', 'Facebook', 'corona', 'chicken1440')

    def test__init__(self):
        '''
		Test to if check the initialization/creation of credential instances is properly done
		'''
        self.assertEqual(self.new_credential.user_name, 'Andy')
        self.assertEqual(self.new_credential.site_name, 'Facebook')
        self.assertEqual(self.new_credential.account_name, 'corona')
        self.assertEqual(self.new_credential.password, 'chicken1440')

    def test_save_credentials(self):
        '''
		Test to check if the new credential info is saved into the credentials list
		'''
        self.new_credential.save_credentials()
        twitter = Credential('Andy', 'Twitter', '', 'chicken1440')
        twitter.save_credentials()
        self.assertEqual(len(Credential.credentials_list), 2)

    def tearDown(self):
        '''
		Function to clear the credentials list after every test
		'''
        Credential.credentials_list = []
        User.users_list = []

    def test_display_credentials(self):
        '''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
        self.new_credential.save_credential()
        twitter = Credential('Andy', 'Twitter', 'corona', 'chicken1440')
        twitter.save_credential()
        gmail = Credential('Andy', 'Gmail', 'corona', 'chicken1440')
        gmail.save_credential()
        self.assertEqual(len(Credential.display_credentials(twitter.user_name)), 3)

    def test_find_by_site_name(self):
        '''
		Test to check if the find_by_site_name method returns the correct credential
		'''
        self.new_credential.save_credential()
        twitter = Credential('Andy', 'Twitter', 'corona', 'chicken1440')
        twitter.save_credentials()
        credential_exists = Credential.find_by_site_name('Twitter')
        self.assertEqual(credential_exists.first_name, twitter.first_name)

    def test_copy_credential(self):
        '''
		Test to check if the copy a credential method copies the correct credential
		'''
        self.new_credential.save_credentials()
        twitter = Credential('Andy', 'Twitter', 'corona', 'chicken1440')
        twitter.save_credentials()
        find_credential = None
        for credential in Credential.user_credentials_list:
            find_credential = Credential.find_by_site_name(credential.site_name)
            return pyperclip.copy(find_credential.password)
        Credential.copy_credential(self.new_credential.site_name)
        self.assertEqual('chicken1440', pyperclip.paste())
        print(pyperclip.paste())

    def test_del_credentials(self):

        self.new_credential.save_credentials()
        twitter = Credential('Andy', 'Twitter', 'corona', 'chicken1440')
        twitter.save_credentials()

        twitter.del_credentials()
        self.assertEqual(len(Credential.credentials_list), 1)


if __name__ == '__main__':
    unittest.main()
