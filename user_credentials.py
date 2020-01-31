
import random
import string

# Global Variables
import pyperclip

global users_list
class User:
'''
Class to make user accounts and save their information
'''
# Class Variables
# global users_list
users_list = []
def __init__(self,first_name,last_name,password):
'''
Method to define the properties for every user object will hold.
'''

# instance variables
self.first_name = first_name
self.last_name = last_name
self.password = password

def save_user(self):
'''
Function to avoid wasting a newly created user instance
'''
User.users_list.append(self)

class Credential:
'''
Class to make account credentials, generate passwords and save their information
'''
# Class Variables
credentials_list =[]
user_credentials_list = []
@classmethod
def check_user(cls,first_name,password):
'''
Method that checks if the name and password entered match entries within the users_list
'''
current_user = ''
for user in User.users_list:
if (user.first_name == first_name and user.password == password):
current_user = user.first_name
return current_user

def __init__(self,user_name,site_name,account_name,password):
'''
Method to define the properties for every user object will hold.
'''

# instance variables
self.user_name = user_name
self.site_name = site_name
self.account_name = account_name
self.password = password

def save_credentials(self):
'''
Function to avoid wasting a newly created user instance
'''
# global users_list
Credential.credentials_list.append(self)

# def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
# '''
# Function to come up with an 8 character password for a credential
# '''
# gen_pass=''.join(random.choice(char) for six in range(size))
# return gen_pass

def del_credentials(self):
Credential.credentials_list.remove(self)

@classmethod
def display_credentials(cls,user_name):
'''
Class method to display the list of credentials saved
'''
user_credentials_list = []
for credential in cls.credentials_list:
if credential.user_name == user_name:
user_credentials_list.append(credential)
return user_credentials_list
				

	

