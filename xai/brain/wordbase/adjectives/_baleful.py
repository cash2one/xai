

#calss header
class _BALEFUL():
	def __init__(self,): 
		self.name = "BALEFUL"
		self.definitions = [u'threatening to do something bad or to hurt someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
