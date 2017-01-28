

#calss header
class _SAGACIOUS():
	def __init__(self,): 
		self.name = "SAGACIOUS"
		self.definitions = [u'having or showing understanding and the ability to make good judgments: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
