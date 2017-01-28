

#calss header
class _MATT():
	def __init__(self,): 
		self.name = "MATT"
		self.definitions = [u'used to describe a surface, colour, or paint that is not shiny: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
