

#calss header
class _UNSAID():
	def __init__(self,): 
		self.name = "UNSAID"
		self.definitions = [u'not said, although thought of or felt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
