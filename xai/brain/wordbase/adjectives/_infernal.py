

#calss header
class _INFERNAL():
	def __init__(self,): 
		self.name = "INFERNAL"
		self.definitions = [u'very bad or unpleasant: ', u'having the qualities of hell (= the place where some people believe bad people go after death): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
