

#calss header
class _COUNTY():
	def __init__(self,): 
		self.name = "COUNTY"
		self.definitions = [u'behaving in a way that is typical of rich people with a high social position who live in large houses in the countryside: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
