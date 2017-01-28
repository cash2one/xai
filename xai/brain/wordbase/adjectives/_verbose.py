

#calss header
class _VERBOSE():
	def __init__(self,): 
		self.name = "VERBOSE"
		self.definitions = [u'using or containing more words than are necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
