class User:
    """a simple attempt to represent a user"""

    def __init__(self, first_name, last_name, birthyear, level):
        """initialize attributes to describe user"""
        self.first = first_name
        self.last = last_name
        self.birthyear = birthyear
        self.level = level
        self.login_attempts = 0

    def describe_user(self):
        """return a description of the user's values"""
        print(f"The user's name is {self.first.title()} {self.last.title()}."
              f"\nTheir birthday is {self.birthyear}."
              f"\nThey are currently on the level {self.level}.")

    def greet_user(self):
        """ returns a simple personalized greeting"""
        print(f"Hello, {self.first.title()}! You are on level {self.level}.")

    def increment_login_attempts(self):
        """increments the login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets the login attempts to 0"""
        self.login_attempts = 0

    def read_login_attempts(self):
        """reads the amount of logins attempted"""
        print(f"You have attempted login {self.login_attempts} times.")


class Admin(User):
    """a simple attempt to model an admin"""

    def __init__(self, first_name, last_name, birthyear, level):
        """ i9nitialize the attributes of an admin """
        super().__init__(first_name, last_name, birthyear, level)
        self.privileges = Privileges()


class Privileges:
    """a simple attempt at modeling privileges for a user"""

    def __init__(self, privileges=('can ban user', 'can mute user', 'can delete post')):
        """ initialize the attributes of Privileges """
        self.privileges = privileges

    def show_privileges(self):
        """ prints a message that shows the admin's privileges """
        print("This user has the following privileges: ")
        for i in self.privileges:
            print(f"{i}")

    def update_privileges(self, update):
        """ updates the privileges of a user """
        self.privileges = update

my_user = User('frank', 'underwood', 1968, 101)
my_user.describe_user()
my_user.greet_user()

my_admin = Admin('francis', 'lee', 1998, 101)
my_admin.privileges.show_privileges()
my_admin.privileges.update_privileges(('can eat shit', 'can breathe fire'))
my_admin.privileges.show_privileges()

