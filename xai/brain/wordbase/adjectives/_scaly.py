

#calss header
class _SCALY():
	def __init__(self,): 
		self.name = "SCALY"
		self.definitions = [u'If skin is scaly, it has small, hard, dry areas that fall off in small pieces: ', u'If the inside of a pipe or container that heats water is scaly, it is covered in a hard white or grey layer of material.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
