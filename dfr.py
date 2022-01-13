#!/bin/python3


class DataFileReader:
	__file_handle = None
	
	def __init__(self,file_name, sep="\t", header=False):
		try:
			self.__file_handle = open(file_name,"rt")  
			self.__delimiter = sep
			self.__header = header
			self.__head_line = ""
			if header:
				self.__head_line = self.__file_handle.readline().strip()
		except:
			print("Error opening file:", file_name)


	def get_head_line(self):
		return self.__head_line

	def get_header(self):
		return tuple(self.__head_line.split(self.__delimiter))

	def get_line(self):
		text = None
		if self.__file_handle != None:
			text = self.__file_handle.readline().strip()                # eine Textzeile lesen
			if text=="":
				self.__file_handle.close()
				self.__file_handle = None
		return text

	def get_data(self):
		line = self.get_line()
		if line != None:
			return line.split(self.__delimiter)
		return None
		
	def get_value(self):
		val = None
		if self.__file_handle != None:
			text = self.__file_handle.readline().strip()                # eine Textzeile lesen
			if len(text) > 0:
				try:
					val = float(text)
				except:
					pass
			else:
				self.__file_handle.close()
				self.__file_handle = None
		return val
	