class TestUser(unittest.TestCase):
    """
        Test class that defines test cases for the user class behaviours.
        Args:
        unittest.TestCase: TestCase class that helps in creating test cases
        """

    def setUp(self):
        self.new_user = User("Andrew", "36135058")

    def tearDown(self):
        User.user_list = []

    def test_init(self):
        self.assertEqual(self.new_user.name, "Andrew")
        self.assertEqual(self.new_user.user_password, "36135058")

    def test_save_user(self):
        """
            test_save_user test case to test if the user object is saved into
            the user list
            add
            """

        self.new_user.save_user()  # saving the new users
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("Andrew1440", "123")  # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        """
            test_delete_user to test if we can remove a user from our users list
            """
        self.new_user.save_user()
        test_user = User("Andrew1440", "chicken123")
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)