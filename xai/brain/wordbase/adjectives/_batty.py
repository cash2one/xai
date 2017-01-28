

#calss header
class _BATTY():
	def __init__(self,): 
		self.name = "BATTY"
		self.definitions = [u'silly and slightly crazy and behaving in a confused way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
