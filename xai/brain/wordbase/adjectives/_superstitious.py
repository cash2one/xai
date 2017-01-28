

#calss header
class _SUPERSTITIOUS():
	def __init__(self,): 
		self.name = "SUPERSTITIOUS"
		self.definitions = [u'based on or believing in superstitions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
