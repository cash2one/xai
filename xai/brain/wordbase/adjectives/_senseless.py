

#calss header
class _SENSELESS():
	def __init__(self,): 
		self.name = "SENSELESS"
		self.definitions = [u'not having good judgment or a good or useful purpose: ', u'unconscious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
