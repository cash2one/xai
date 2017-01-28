

#calss header
class _NAMELESS():
	def __init__(self,): 
		self.name = "NAMELESS"
		self.definitions = [u'having no name, or having a name that is not known: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
