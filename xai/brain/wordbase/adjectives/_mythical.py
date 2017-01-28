

#calss header
class _MYTHICAL():
	def __init__(self,): 
		self.name = "MYTHICAL"
		self.definitions = [u'existing only in stories: ', u'imaginary or not real: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
