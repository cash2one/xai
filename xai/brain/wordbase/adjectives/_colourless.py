

#calss header
class _COLOURLESS():
	def __init__(self,): 
		self.name = "COLOURLESS"
		self.definitions = [u'having no colour: ', u'not exciting or not interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
