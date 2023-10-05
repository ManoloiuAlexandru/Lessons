class Car:
    def __init__(self, mark, engine, year, km, price):
        self.mark = mark
        self.engine = engine
        self.year = year
        self.km = km
        self.price = price

  class CreditCard:
    def __init__(self, card_number, cardholder_name, exp_date, name_of_the_bank):
        self.card_number = card_number
        self.cardholder_name = cardholder_name
        self.exp_date = exp_date
        self.name_of_the_bank = name_of_the_bank

    def validate_card(self):
        """
        Check if card number is valid (Luhn Number Checksum)
        """

    class NetworkDevice:
    def __init__(self, name, IP, vendor, serial_number):
        self.name = name
        self.IP = IP
        self.vendor = vendor
        self.serial_number = serial_number
    
    def validation_ip(self):
        """
        Check if IP is valid
        """

    class Password:
    def __init__(self, password_contains):
        self.password_contains = password_contains
        self.security = None

    def check_security(self):
        """
        Check if the password is strong,week or medium based on the general standards
        """
        pass
