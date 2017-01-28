

#calss header
class _MARIAN():
	def __init__(self,): 
		self.name = "MARIAN"
		self.definitions = [u'relating to the Virgin Mary, the mother of Jesus Christ: ', u'relating to the period when Queen Mary I was queen of England, from 1553 to 1558: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
