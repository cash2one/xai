

#calss header
class _CRABBED():
	def __init__(self,): 
		self.name = "CRABBED"
		self.definitions = [u'Crabbed writing is written too closely together and therefore difficult to read.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
