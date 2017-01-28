

#calss header
class _NEATLY():
	def __init__(self,): 
		self.name = "NEATLY"
		self.definitions = [u'in a tidy way: ', u'in a clever and simple way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
