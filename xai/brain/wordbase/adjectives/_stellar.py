

#calss header
class _STELLAR():
	def __init__(self,): 
		self.name = "STELLAR"
		self.definitions = [u'of a star or stars: ', u'Stellar people or activities are of an extremely high standard: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
