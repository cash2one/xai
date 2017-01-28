

#calss header
class _LETTER():
	def __init__(self,): 
		self.name = "LETTER"
		self.definitions = [u'used to refer to a standard size of paper in the US, 8.5 inches by 11 inches: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
