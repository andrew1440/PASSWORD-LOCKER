import unittest
from password import User, Credential
class TestCredential(unittest.TestCase):
    """
        Test class that defines test cases for the credential class behaviours.
        Args:
        unittest.TestCase: TestCase class that helps in creating test cases
        """

    def setUp(self):
        self.new_credential = Credential("facebook", "Andrew1440", "chicken123")

    def tearDown(self):
        Credential.credential_list = []

    def test_init(self):
        self.assertEqual(self.new_credential.account, "facebook")
        self.assertEqual(self.new_credential.account_username, "Andrew1440")
        self.assertEqual(self.new_credential.account_password, "chicken123")

    def test_save_credential(self):
        """
            test_save_credential test case to test if the credential object is saved into
            the credential list
            add
            """
        self.new_credential.test_save_credential()  # saving the new credential
        self.assertEqual(len(Credential.credential_list), 0)

    def test_save_multiple_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential("Twitter", "Corona", "chicken123")  # new credential
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credential(self):
        """
        test_delete_credential to test if we can remove a credential from our credential list
        """
        self.new_credential.save_credential()
        test_credential = Credential("facebook", "Andrew1440", "chicken123")
        test_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)
    def test_find_credential_by_account_username(self):
        self.new_credential.save_credential()
        test_credential = Credential("facebook", "Andrew1440", "chicken123")
        test_credential.save_credential()
        found_credential =Credential.find_by_account_username("Andrew1440")
        self.assertEqual(found_credential.account_password, test_credential.account_password)

    def test_credential_exists(self):
        self.new_credential.save_credential()
        test_credential = Credential("facebook", "Andrew1440", "chicken123")
        test_credential.save_credential()
        credential_exists = Credential.credential_exists("Andrew1440")
        self.assertTrue(credential_exists)
        
    def test_display_all_credentials(self):
        self.assertEqual(Credential.display_credentials(), Credential.credential_list)

if __name__ == '__main__':
    unittest.main()