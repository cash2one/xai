

#calss header
class _FLIP():
	def __init__(self,): 
		self.name = "FLIP"
		self.definitions = [u'informal for  flippant ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
