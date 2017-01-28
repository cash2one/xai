

#calss header
class _FREIGHT():
	def __init__(self,): 
		self.name = "FREIGHT"
		self.definitions = [u'transported as part of a large group of things, by ship, aircraft, train, or truck: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
