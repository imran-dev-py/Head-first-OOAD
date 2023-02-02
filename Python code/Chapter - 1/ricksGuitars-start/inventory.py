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
        for guitar in self.guitars:
            # ignore serial number since that's unique
            # ignore price since that's unique
        
            builder = search_guitar.get_builder()
            if (builder is not None and not builder == '') and (not builder == guitar.get_builder()):
                continue
            
            model = search_guitar.get_model()
            if (model is not None and not model == '') and (not model == guitar.get_model()):
                continue
            
            type_ = search_guitar.get_type()
            if (type_ is not None and not type_ == '') and (not type_ == guitar.get_type()):
                continue
            
            back_wood = search_guitar.get_back_wood()
            if (back_wood is not None and not back_wood == '') and (not back_wood == guitar.get_back_wood()):
                continue

            top_wood = search_guitar.get_top_wood()
            if (top_wood is not None and not top_wood == '') and (not top_wood == guitar.get_top_wood()):
                continue
            
            return guitar
        
        return None
    