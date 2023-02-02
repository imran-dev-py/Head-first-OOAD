class GuitarSpec:
	def __init__(self, builder, type_, model, back_wood, top_wood):
		self.__builder = builder
		self.__type_ = type_
		self.__top_wood = top_wood
		self.__back_wood = back_wood
		self.__model = model

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

	



