class Restaurant:
    """
    a simple attempt to represent a restaurant
    """
    def __init__(self, name, cuisine):
        """
        :param name: str, restaurant name
        :param cuisine: str, type of cuisine
        """
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """
        :return: prints the name and cuisine type of the restaurant
        """
        print(f"{self.name.title()} is the name of the restaurant. "
              f"\nThe restaurant serves this type of food: {self.cuisine}")

    def open_restaurant(self):
        """
        :return: prints a msg indicating the restaurant is open
        """
        print(f"{self.name.title()} is now open!")

    def read_number_served(self):
        """ reads the number of customers served"""
        print(f"This restaurant has served {self.number_served} customers.")

    def set_number_served(self, customers):
        """ sets the amount of customers served"""
        self.number_served = customers

    def increment_number_served(self, sales):
        """ increments the amount of customers served"""
        self.number_served += sales


class IceCreamStand(Restaurant):
    """ a simple ice cream stand in the model of a restaurant """

    def __init__(self, name, cuisine, flavours):
        """ initialize the ice cream stand's attributes """
        super(IceCreamStand, self).__init__(name, cuisine)
        self.flavours = flavours

    def describe_flavours(self):
        """ prints out the list of ice cream flavours """
        print(f"This ice cream stand has the following flavours:")
        for flavour in self.flavours:
            print(f"{flavour}")


my_ice_cream_stand = IceCreamStand('rocky point', 'ice cream', ['chocolate', 'vanilla', 'strawberry'])
my_ice_cream_stand.describe_flavours()
my_ice_cream_stand.describe_restaurant()