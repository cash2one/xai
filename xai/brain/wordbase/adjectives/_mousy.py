

#calss header
class _MOUSY():
	def __init__(self,): 
		self.name = "MOUSY"
		self.definitions = [u'Mousy hair is brown and not special or attractive.', u'shy and nervous and having few interesting qualities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
