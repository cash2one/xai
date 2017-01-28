

#calss header
class _GODFORSAKEN():
	def __init__(self,): 
		self.name = "GODFORSAKEN"
		self.definitions = [u'A godforsaken place is not attractive and contains nothing interesting or pleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
