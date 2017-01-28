

#calss header
class _FECUND():
	def __init__(self,): 
		self.name = "FECUND"
		self.definitions = [u'able to produce a lot of crops, fruit, babies, young animals, etc.: ', u'producing or creating a lot of new things, ideas, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
