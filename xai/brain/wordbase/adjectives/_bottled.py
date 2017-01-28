

#calss header
class _BOTTLED():
	def __init__(self,): 
		self.name = "BOTTLED"
		self.definitions = [u'contained, stored, or sold in bottles: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
