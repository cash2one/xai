

#calss header
class _FETID():
	def __init__(self,): 
		self.name = "FETID"
		self.definitions = [u'smelling extremely bad and stale: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
