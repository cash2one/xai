

#calss header
class _COGNATE():
	def __init__(self,): 
		self.name = "COGNATE"
		self.definitions = [u'Cognate languages and words have the same origin, or are related and in some way similar: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
