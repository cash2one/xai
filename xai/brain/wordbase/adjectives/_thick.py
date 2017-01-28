

#calss header
class _THICK():
	def __init__(self,): 
		self.name = "THICK"
		self.definitions = [u'having a large distance between two sides: ', u'growing close together and in large amounts: ', u'difficult to see through: ', u'(of a liquid) not flowing easily: ', u'stupid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
