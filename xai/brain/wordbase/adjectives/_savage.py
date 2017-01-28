

#calss header
class _SAVAGE():
	def __init__(self,): 
		self.name = "SAVAGE"
		self.definitions = [u'extremely violent, wild, or frightening: ', u'very serious or cruel: ', u'very large and severe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
