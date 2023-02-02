from guitar import Guitar 


class Inventory:
    def __init__(self):
        self.guitars = list()
    
    def add_guitar(self, serial_number, price, builder, model, type_, back_wood, top_wood):
        guitar = Guitar(serial_number, price, builder, model, type_, back_wood, top_wood)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in guitars:
            if guitar.serial_number == serial_number:
                return guitar
        
        return None
    
    def search(self, search_guitar):
        matching_guitars = list()

        for guitar in self.guitars:
            # ignore serial number since that's unique
            # ignore price since that's unique
        
            builder = search_guitar.get_builder()
            if builder != guitar.get_builder():
                continue
            
            model = search_guitar.get_model().lower()
            if (model is not None and not model == '') and (not model == guitar.get_model().lower()):
                continue
            
            type_ = search_guitar.get_type()
            if type_ != guitar.get_type():
                continue
            
            back_wood = search_guitar.get_back_wood()
            if (back_wood != guitar.get_back_wood()):
                continue

            top_wood = search_guitar.get_top_wood()
            if top_wood != guitar.get_top_wood():
                continue
            
            matching_guitars.append(guitar)
        
        return matching_guitars
    