

#calss header
class _EROGENOUS():
	def __init__(self,): 
		self.name = "EROGENOUS"
		self.definitions = [u'of areas of the body, able to feel sexual pleasure: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
