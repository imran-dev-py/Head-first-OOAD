from guitar import Guitar 


class Inventory:
    def __init__(self):
        self.guitars = list()
    
    def add_guitar(self, serial_number, price, spec):
        guitar = Guitar(serial_number, price, spec)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in guitars:
            if guitar.serial_number == serial_number:
                return guitar
        
        return None
    
    def search(self, search_spec):
        matching_guitars = list()

        for guitar in self.guitars:
            guitar_spec = guitar.get_spec()
        
            if guitar_spec.matches(search_spec):
                matching_guitars.append(guitar)
        
        return matching_guitars
    