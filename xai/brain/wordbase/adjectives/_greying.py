

#calss header
class _GREYING():
	def __init__(self,): 
		self.name = "GREYING"
		self.definitions = [u'used to describe a person whose hair is becoming grey or white, or the hair itself: ', u'containing an increasing number of older people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
