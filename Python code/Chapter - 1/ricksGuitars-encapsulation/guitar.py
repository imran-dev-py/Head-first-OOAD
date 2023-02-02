from guitar_spec import GuitarSpec


class Guitar:
    def __init__(self, serial_number, price, builder, model, type_, back_wood, top_wood):
        self.__serial_number = serial_number
        self.__price = price
        self.__spec = GuitarSpec(builder, model, type_, back_wood, top_wood)
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        self.__price = new_price
    
    def get_spec(self):
        return self.__spec
