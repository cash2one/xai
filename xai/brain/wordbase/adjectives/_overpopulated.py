

#calss header
class _OVERPOPULATED():
	def __init__(self,): 
		self.name = "OVERPOPULATED"
		self.definitions = [u'If a country or city, etc. is overpopulated, it has too many people for the amount of food, materials, and space available there.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
