

#calss header
class _DOUBLY():
	def __init__(self,): 
		self.name = "DOUBLY"
		self.definitions = [u'twice as much, or very much more: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
