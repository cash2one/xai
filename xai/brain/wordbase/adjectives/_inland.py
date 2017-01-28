

#calss header
class _INLAND():
	def __init__(self,): 
		self.name = "INLAND"
		self.definitions = [u'in the middle of a country, away from the sea: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
