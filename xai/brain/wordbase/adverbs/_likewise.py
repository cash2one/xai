

#calss header
class _LIKEWISE():
	def __init__(self,): 
		self.name = "LIKEWISE"
		self.definitions = [u'in the same way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
