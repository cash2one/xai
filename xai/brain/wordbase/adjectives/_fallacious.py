

#calss header
class _FALLACIOUS():
	def __init__(self,): 
		self.name = "FALLACIOUS"
		self.definitions = [u'not correct: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
