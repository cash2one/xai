

#calss header
class _MENTHOLATED():
	def __init__(self,): 
		self.name = "MENTHOLATED"
		self.definitions = [u'containing menthol as a flavour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
