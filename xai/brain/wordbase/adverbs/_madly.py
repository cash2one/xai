

#calss header
class _MADLY():
	def __init__(self,): 
		self.name = "MADLY"
		self.definitions = [u'with a lot of energy and enthusiasm: ', u'to love someone very much: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
