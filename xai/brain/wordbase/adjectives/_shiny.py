

#calss header
class _SHINY():
	def __init__(self,): 
		self.name = "SHINY"
		self.definitions = [u'A shiny surface is bright because it reflects light: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
