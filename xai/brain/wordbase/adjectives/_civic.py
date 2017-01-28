

#calss header
class _CIVIC():
	def __init__(self,): 
		self.name = "CIVIC"
		self.definitions = [u'of a town or city or the people who live in it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
