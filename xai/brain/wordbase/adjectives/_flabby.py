

#calss header
class _FLABBY():
	def __init__(self,): 
		self.name = "FLABBY"
		self.definitions = [u'soft and fat: ', u'weak and without force: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
