

#calss header
class _WOODY():
	def __init__(self,): 
		self.name = "WOODY"
		self.definitions = [u'like wood, for example in taste or smell', u'Woody plants have hard stems: ', u'having many trees: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
