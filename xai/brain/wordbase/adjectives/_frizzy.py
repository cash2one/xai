

#calss header
class _FRIZZY():
	def __init__(self,): 
		self.name = "FRIZZY"
		self.definitions = [u'(of hair) very curly and not smooth or shiny: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
