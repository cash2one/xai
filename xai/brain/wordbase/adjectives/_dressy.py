

#calss header
class _DRESSY():
	def __init__(self,): 
		self.name = "DRESSY"
		self.definitions = [u'Dressy clothes are suitable for formal occasions: ', u'A dressy occasion is one at which people wear very formal clothes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
