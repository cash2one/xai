

#calss header
class _FEEBLE():
	def __init__(self,): 
		self.name = "FEEBLE"
		self.definitions = [u'weak and without energy, strength, or power: ', u'not effective or good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
