

#calss header
class _MUSTY():
	def __init__(self,): 
		self.name = "MUSTY"
		self.definitions = [u'smelling unpleasantly old and slightly wet: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
