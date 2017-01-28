

#calss header
class _FIXEDLY():
	def __init__(self,): 
		self.name = "FIXEDLY"
		self.definitions = [u'to look continuously at one thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
