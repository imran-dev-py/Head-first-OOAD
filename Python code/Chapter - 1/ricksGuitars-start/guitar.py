class Guitar:
    def __init__(self, serial_number, price, builder, model, type_, back_wood, top_wood):
        self.__serial_number = serial_number
        self.__price = price
        self.__builder = builder
        self.__model = model
        self.__type_ = type_
        self.__top_wood = top_wood
        self.__back_wood = back_wood
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        self.__price = new_price
    
    def get_builder(self):
        return self.__builder
    
    def get_model(self):
        return self.__model
    
    def get_type(self):
        return self.__type_ 
    
    def get_back_wood(self):
        return self.__back_wood
    
    def get_top_wood(self):
        return self.__top_wood
