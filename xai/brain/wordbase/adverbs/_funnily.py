

#calss header
class _FUNNILY():
	def __init__(self,): 
		self.name = "FUNNILY"
		self.definitions = [u'strangely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
