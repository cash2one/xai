

#calss header
class _SIMPLISTIC():
	def __init__(self,): 
		self.name = "SIMPLISTIC"
		self.definitions = [u'making something complicated seem simple by ignoring important parts of it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
