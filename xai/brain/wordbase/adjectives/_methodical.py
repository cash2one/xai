

#calss header
class _METHODICAL():
	def __init__(self,): 
		self.name = "METHODICAL"
		self.definitions = [u'Methodical people do things in a very ordered, careful way: ', u'done in a very ordered, careful way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
