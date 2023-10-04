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
