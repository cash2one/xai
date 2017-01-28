

#calss header
class _LUXURIANT():
	def __init__(self,): 
		self.name = "LUXURIANT"
		self.definitions = [u'growing thickly, strongly, and well: ', u'pleasantly thick or full: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
