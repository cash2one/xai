

#calss header
class _EMERGING():
	def __init__(self,): 
		self.name = "EMERGING"
		self.definitions = [u'starting to exist: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
