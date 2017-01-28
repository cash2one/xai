

#calss header
class _ASIATIC():
	def __init__(self,): 
		self.name = "ASIATIC"
		self.definitions = [u'relating to Asia, especially when considering its geography or its plants and animals, rather than social or cultural matters: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
