

#calss header
class _NUBILE():
	def __init__(self,): 
		self.name = "NUBILE"
		self.definitions = [u'A nubile woman is young and sexually attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
