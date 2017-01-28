

#calss header
class _TEXTBOOK():
	def __init__(self,): 
		self.name = "TEXTBOOK"
		self.definitions = [u'(of an example of something) extremely good, or thought to be usual or typical: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
