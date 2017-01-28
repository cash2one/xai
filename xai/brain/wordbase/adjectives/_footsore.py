

#calss header
class _FOOTSORE():
	def __init__(self,): 
		self.name = "FOOTSORE"
		self.definitions = [u'having painful, tired feet, especially after a lot of walking']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
