

#calss header
class _LEADED():
	def __init__(self,): 
		self.name = "LEADED"
		self.definitions = [u'Leadedpetrol (= fuel) has small amounts of lead in it.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
