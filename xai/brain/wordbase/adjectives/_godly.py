

#calss header
class _GODLY():
	def __init__(self,): 
		self.name = "GODLY"
		self.definitions = [u'obeying and respecting God: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
