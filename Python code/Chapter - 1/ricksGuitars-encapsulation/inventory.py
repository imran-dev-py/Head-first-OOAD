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
    
    def search(self, search_spec):
        matching_guitars = list()

        for guitar in self.guitars:
            guitar_spec = guitar.get_spec()
        
            builder = search_spec.get_builder()
            if builder != guitar_spec.get_builder():
                continue
            
            model = search_spec.get_model().lower()
            if (model is not None and not model == '') and (not model == guitar_spec.get_model().lower()):
                continue
            
            type_ = search_spec.get_type()
            if type_ != guitar_spec.get_type():
                continue
            
            back_wood = search_spec.get_back_wood()
            if (back_wood != guitar_spec.get_back_wood()):
                continue

            top_wood = search_spec.get_top_wood()
            if top_wood != guitar_spec.get_top_wood():
                continue
            
            matching_guitars.append(guitar)
        
        return matching_guitars
    