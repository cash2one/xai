

#calss header
class _PRETTY():
	def __init__(self,): 
		self.name = "PRETTY"
		self.definitions = [u'quite, but not extremely: ', u'almost: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
