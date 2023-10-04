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
