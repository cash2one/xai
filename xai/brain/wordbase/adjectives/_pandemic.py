

#calss header
class _PANDEMIC():
	def __init__(self,): 
		self.name = "PANDEMIC"
		self.definitions = [u'(of a disease) existing in almost all of an area or in almost all of a group of people, animals, or plants: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
