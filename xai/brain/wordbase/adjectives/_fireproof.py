

#calss header
class _FIREPROOF():
	def __init__(self,): 
		self.name = "FIREPROOF"
		self.definitions = [u'unable to be damaged by fire: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
