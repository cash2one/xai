

#calss header
class _DIVERSE():
	def __init__(self,): 
		self.name = "DIVERSE"
		self.definitions = [u'including many different types of people or things: ', u'very different from each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
