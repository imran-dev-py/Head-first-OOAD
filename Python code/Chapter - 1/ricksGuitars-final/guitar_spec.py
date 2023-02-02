class GuitarSpec:
	def __init__(self, builder, type_, model, back_wood, top_wood, num_strings):
		self.__builder = builder
		self.__type_ = type_
		self.__top_wood = top_wood
		self.__back_wood = back_wood
		self.__model = model
		self.__num_strings = num_strings

	def get_builder(self):
		return self.__builder

	def get_type(self):
		return self.__type_

	def get_back_wood(self):
		return self.__back_wood

	def get_top_wood(self):
		return self.__top_wood

	def get_model(self):
		return self.__model

	def get_num_strings(self):
		return self.__num_strings

	def matches(self, search_spec):
		builder = search_spec.get_builder()
		if self.get_builder() != builder:
		    return False
        
		model = search_spec.get_model().lower()
		if (model is not None and not model == '') and (not model == self.get_model().lower()):
		    return False

		type_ = search_spec.get_type()
		if self.get_type() != type_:
		    return False

		back_wood = search_spec.get_back_wood()
		if (self.get_back_wood() != back_wood):
		    return False

		top_wood = search_spec.get_top_wood()
		if self.get_top_wood() != top_wood:
		    return False

		num_strings = search_spec.get_num_strings()
		if self.get_num_strings() != num_strings:
			return False

		return True 

	



