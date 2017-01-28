

#calss header
class _HUMBLY():
	def __init__(self,): 
		self.name = "HUMBLY"
		self.definitions = [u'in a way that shows that you do not think you are important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
