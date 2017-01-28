

#calss header
class _BULBOUS():
	def __init__(self,): 
		self.name = "BULBOUS"
		self.definitions = [u'If a part of the body is bulbous, it is fat and round: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
