

#calss header
class _LIKEABLE():
	def __init__(self,): 
		self.name = "LIKEABLE"
		self.definitions = [u'A likeable person is pleasant and easy to like: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
