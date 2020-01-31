import unittest # Importing the unittest module
from credential import Credential # Importing the credential class

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
     # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Andy","Corona","0712345678","Andy@ms.com") # create credential object
    

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.first_name,"Andy")
        self.assertEqual(self.new_credential.last_name,"Corona")
        self.assertEqual(self.new_credential.phone_number,"0712345678")
        self.assertEqual(self.new_credential.email,"Andy@ms.com")


    def test_save_credential(self):
        '''
        test_save_credential test case to test if the contact object is saved into
        the contact list
        '''
        self.new_credential.test_save_credential() # saving the new contact
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential
        objects to our credential_list
        '''
        self.new_credential.test_save_credential()
        test_save_credential = Credential("Test","user","0712345678","test@user.com") # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []

    # other test cases here
    def test_save_multiple_credential(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","0712345678","test@user.com") # new contact
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)
            # More tests above
    def test_delete_credential(self):
            '''
            test_delete_credential to test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","0712345678","test@user.com") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)
    def delete_credential(self):

            '''
            delete_credential method deletes a saved credential from the credential_list
            '''

    def test_find_credential_by_number(self):
            '''
            test to check if we can find a credential by phone number and display information
            '''

            self.new_credential.save_credential()
            test_credential = Credential("Test","user","0711223344","test@user.com") # new credential
            test_credential.save_credential()

            found_credential = Credential.find_by_number("0711223344")

            self.assertEqual(found_credential.email,test_credential.email)
        @classmethod
        def find_by_number(cls,number):
            '''
            Method that takes in a number and returns a credential that matches that number.

            Args:
                number: Phone number to search for
            Returns :
                Credential of person that matches the number.
            '''

        for credential in cls.credential_list:
                if credential.phone_number == number:
                    return credential

   def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","0711223344","test@user.com") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("0711223344")

        self.assertTrue(credential_exists)

if __name__ == '__main__':
    unittest.main()