

#calss header
class _MOMENTARILY():
	def __init__(self,): 
		self.name = "MOMENTARILY"
		self.definitions = [u'for a very short time: ', u'very soon: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
